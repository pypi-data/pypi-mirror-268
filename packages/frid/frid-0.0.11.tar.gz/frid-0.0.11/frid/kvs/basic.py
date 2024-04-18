"""This class implement a basic value store that retrives the whole data then do selection.
It will derive a memory based store from there
"""
import threading
from abc import abstractmethod
from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import TypeVar, cast


from ..typing import MISSING, PRESENT, FridBeing, FridMapVT, FridValue, MissingType, StrKeyMap
from ..guards import is_frid_array
from ..helper import frid_merge
from ..strops import escape_control_chars
from .store import VSPutFlag, VStoreKey, VStoreSel, ValueStore

_T = TypeVar('_T')

class SimpleValueStore(ValueStore):
    @abstractmethod
    def _get(self, key: str) -> FridValue:
        """Get the whole data from the store associated to the given `key`."""
        raise NotImplementedError
    @abstractmethod
    def _put(self, key: str, val: FridValue) -> bool:
        """Write the whole data into the store associated to the given `key`."""
        raise NotImplementedError
    @abstractmethod
    def _rmw(self, key: str, mod: Callable[...,tuple[FridValue|FridBeing,_T]],
             *args, **kwargs) -> _T:
        """The read-modify-write process through a modification callback `mod`.
        - Returns a pair, first is the boolean state of put, and the second from proc.
        The callback accepting a single nullable text string as input and returns a pair of
        nullable string and an integer value. The first is written to the store (if not None),
        and the second is returned if the put operation succeeds.
        """
        raise NotImplementedError
    @abstractmethod
    def _del(self, key: str) -> bool:
        """Delete the data in the store associated to the given `key`."""
        raise NotImplementedError

    def _key(self, key: VStoreKey) -> str:
        if isinstance(key, str):
            return key
        if isinstance(key, tuple):
            return '\t'.join(escape_control_chars(str(k)) for k in key)
        raise ValueError(f"Invalid key type {type(key)}")

    def _fix_indexes(self, sel: tuple[int,int], val: Sequence):
        (index, until) = sel
        if not len(sel) == 2 or not isinstance(index, int) or not isinstance(until, int):
            raise ValueError(f"Invalid selector: {sel}")
        if index < 0:
            index += len(val)
            if index < 0:
                index = 0
        if until <= 0:
            until += len(val)
            if until < 0:
                until = 0
        return (index, until)

    def _get_sel_seq(
            self, val: Sequence, sel: int|slice|tuple[int,int]
    ) -> FridValue|MissingType:
        if isinstance(sel, int):
            return val[sel] if 0 <= sel < len(val) else MISSING
        if isinstance(sel, slice):
            return val[sel]
        if isinstance(sel, tuple) and len(sel) == 2:
            (index, until) = self._fix_indexes(sel, val)
            return val[index:until]
        raise ValueError(f"Invalid selector type {type(sel)}")
    def _get_sel_map(
            self, val: StrKeyMap, sel: str|Iterable[str]
    ) -> StrKeyMap|FridValue|MissingType:
        if sel is None:
            return val
        if isinstance(sel, str):
            out = val.get(sel, MISSING)
            assert out is not PRESENT
            return out
        if isinstance(sel, Iterable):
            return {k: v for k in val if not isinstance((v := val.get(k)), FridBeing)}
        raise ValueError(f"Invalid selector type {type(sel)}")
    def _get_sel(self, val: FridValue, sel: VStoreSel) -> FridValue|MissingType:
        if sel is None:
            return val
        if isinstance(val, Mapping):
            return self._get_sel_map(val, cast(str|Iterable[str], sel))
        if isinstance(val, Sequence):
            return self._get_sel_seq(val, cast(int|slice|tuple[int,int], sel))
        raise ValueError(f"Selector is not None for data type {type(val)}")
    def _add(self, old: FridValue|MissingType, new: FridValue,
             flags: VSPutFlag) -> tuple[FridValue|FridBeing,bool]:
        if old is MISSING:
            return (MISSING, False) if flags & VSPutFlag.NO_CREATE else (new, True)
        if flags & VSPutFlag.NO_CHANGE:
            return (PRESENT, False)
        if flags & VSPutFlag.KEEP_BOTH:
            return (frid_merge(old, new), True)
        return (new, True)
    def _del_sel_list(self, val: list, sel: int|slice|tuple[int,int]) -> int:
        if isinstance(sel, int):
            if 0 <= sel < len(val):
                del val[sel]
                return 1
            return 0
        if isinstance(sel, slice):
            del val[sel]
        if isinstance(sel, tuple):
            (index, until) = self._fix_indexes(sel, val)
            old_len = len(val)
            del val[index:until]
            return len(val) - old_len
        raise ValueError(f"Invalid sequence selector type {type(sel)}")
    def _del_sel_dict(self, val: dict[str,FridMapVT], sel: str|Iterable[str]) -> int:
        if isinstance(sel, str):
            return 0 if val.pop(sel, MISSING) is MISSING else 1
        return sum(bool(val.pop(k, MISSING) is not MISSING) for k in val)
    def _del_sel(self, val: FridValue, sel: VStoreSel) -> tuple[FridValue,int]:
        assert sel is not None
        if isinstance(val, Mapping):
            val = dict(val)
            return (val, self._del_sel_dict(val, cast(str|Iterable[str], sel)))
        if is_frid_array(val):
            val = list(val)
            return (val, self._del_sel_list(val, cast(int|slice|tuple[int,int], sel)))
        raise ValueError(f"Data type {type(val)} does not support partial removal")

    def get_frid(self, key: VStoreKey, sel: VStoreSel=None) -> FridValue|MissingType:
        key = self._key(key)
        with self:
            return self._get_sel(self._get(key), sel)
    def put_frid(self, key: VStoreKey, val: FridValue, /, flags: VSPutFlag) -> int|bool:
        key = self._key(key)
        with self:
            if flags == VSPutFlag.ALWAYS_PUT:
                return self._put(key, val)
            return self._rmw(key, self._add, val, flags)
    def del_frid(self, key: VStoreKey, sel: VStoreSel=None, /) -> int|bool:
        key = self._key(key)
        with self:
            if sel is None:
                return self._del(key)
            return self._rmw(key, self._del_sel, sel)

class MemoryValueStore(SimpleValueStore):
    StorageType = dict[tuple[str,...],tuple[threading.Lock,dict[str,FridValue]]]

    def __init__(self, store: StorageType|None=None, names: tuple[str,...]=()):
        super().__init__()
        if store is None:
            store = {}
        self._store = store
        (self._lock, self._data) = store.setdefault(names, (threading.Lock(), {}))

    def get_data(self):
        return self._data

    def substore(self, name: str, *args: str) -> 'MemoryValueStore':
        return __class__(self._store, (name, *args))

    def _get(self, key: str, /) -> FridValue|MissingType:
        return self._data.get(key, MISSING)
    def _rmw(self, key: str, mod: Callable[...,tuple[FridValue|FridBeing,_T]],
             *args, **kwargs) -> _T:
        old_data = self._data.get(key, MISSING)
        (data, out) = mod(old_data, *args, **kwargs)
        if not isinstance(data, FridBeing):
            self._data[key] = data
        elif data is MISSING and old_data is not MISSING:
            del self._data[key]
        return out
    def _put(self, key: str, data: FridValue, /, *, update: bool=False) -> bool:
        if not update and key in self._data:
            return False
        self._data[key] = data
        return True
    def _del(self, key: str) -> bool:
        return self._data.pop(key, MISSING) is not MISSING

