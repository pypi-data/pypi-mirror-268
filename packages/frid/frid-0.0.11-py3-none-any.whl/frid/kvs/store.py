"""The Frid Value Store."""

import asyncio
from abc import ABC, abstractmethod
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from enum import Flag
from typing import Literal, Mapping, NamedTuple, TypeVar


from ..typing import MISSING, BlobTypes, FridArray, FridBeing, FridValue, MissingType, StrKeyMap
from ..guards import as_kv_pairs, is_frid_array, is_frid_skmap

VStoreKey = str|tuple[str|int,...]|NamedTuple
VSListSel = int|slice|tuple[int,int]|None
VSDictSel = str|Iterable[str]|None
VStoreSel = VSListSel|VSDictSel
VStorePutBulkData = Mapping[VStoreKey,FridValue]|Sequence[tuple[VStoreKey,FridValue]]|Iterable

class VSPutFlag(Flag):
    ALWAYS_PUT = 0   # Special value to skip all the checks
    NO_CREATE = 0x80    # Do not create a new entry
    NO_CHANGE = 0x40    # Do not change existing entry; skip all following if set
    KEEP_BOTH = 0x20    # Keep both existing data and new data, using frid_merge()
    # TODO additional flags to pass to for frid_merge()

@dataclass
class StoreEntryMetaData:
    name: str
    type: Literal['text', 'blob', 'list', 'dict', 'real', 'date', 'null', 'bool']
    size: int

class ValueStore(ABC):
    def __enter__(self):
        return self
    def __exit__(self, typ, val, tb):
        pass
    def __aenter__(self):
        return self
    def __aexit__(self, typ, val, tb):
        pass

    @abstractmethod
    def substore(self, name: str, *args: str) -> 'ValueStore':
        """Returns a substore ValueStore as given by a list of names."""
        raise NotImplementedError

    def get_meta(self, keys: Iterable[VStoreKey]) -> Mapping[str,StoreEntryMetaData]:
        """Gets the meta data of a list of `keys` and returns a map for existing keys.
        Notes: There is no atomicity guarantee for this method.
        """
        raise NotImplementedError
    _T = TypeVar('_T')
    def get_frid(self, key: VStoreKey, sel: VStoreSel=None) -> FridValue|MissingType:
        """Gets the value of the given `key` in the value store.
        - If `sel` is specified, use the selection rule to select the partial data to return.
        - If the value of the key is missing, return MISSING.
        """
        raise NotImplementedError
    def put_frid(self, key: VStoreKey, val: FridValue, /, flags: VSPutFlag) -> int|bool:
        """Puts the value `val` into the store for the given `key`.
        """
        raise NotImplementedError
    def del_frid(self, key: VStoreKey, sel: VStoreSel=None, /) -> int|bool:
        """Deletes the data associated with the given `key` from the store.
        - Returns the number of entries deleted if the selector `sel` is not None.
        - If the selector `sel` is None, a boolean to indicate if anything
          is deleted.
        """
        raise NotImplementedError
    def get_bulk(self, keys: Iterable[VStoreKey], /) -> FridArray:
        """Returns the data associated with a list of keys in the store."""
        with self:
            return [v for k in keys if (v := self.get_frid(k)) is not MISSING]
    def put_bulk(self, data: VStorePutBulkData, /, flags) -> int:
        """Put the data in the into the store.
        - `data`: either a key/value pairs or a list of tuple of key/value pairs
        """
        with self:
            return sum(int(self.put_frid(k, v, flags)) for k, v in as_kv_pairs(data))
    def del_bulk(self, keys: Iterable[VStoreKey]) -> int:
        with self:
            return sum(int(self.del_frid(k)) for k in keys)

    def get_text(self, key: VStoreKey, alt: _T=None) -> str|_T:
        data = self.aget_frid(key)
        if data is MISSING:
            return alt
        assert isinstance(data, str)
        return data
    def get_blob(self, key: VStoreKey, alt: _T=None) -> BlobTypes|_T:
        data = self.aget_frid(key)
        if data is MISSING:
            return alt
        assert isinstance(data, BlobTypes)
        return data
    def get_list(self, key: VStoreKey, sel: VSListSel=None, alt: _T=None) -> FridArray|_T:
        data = self.aget_frid(key, sel)
        if data is MISSING:
            return alt
        assert is_frid_array(data)
        return data
    def get_dict(self, key: VStoreKey, sel: VSDictSel=None, alt: _T=None) -> StrKeyMap|_T:
        data = self.aget_frid(key, sel)
        if data is MISSING:
            return alt
        assert is_frid_skmap(data)
        return data

    async def aget_meta(self, keys: Iterable[VStoreKey]) -> Mapping[str,StoreEntryMetaData]:
        raise NotImplementedError
    async def aget_frid(self, key: VStoreKey, sel: VStoreSel=None) -> FridValue|MissingType:
        raise NotImplementedError
    async def aput_frid(self, key: VStoreKey, val: FridValue, /, flags: VSPutFlag) -> int|bool:
        raise NotImplementedError
    async def adel_frid(self, key: VStoreKey, sel: VStoreSel=None, /) -> int|bool:
        raise NotImplementedError
    async def aget_bulk(self, keys: Iterable[VStoreKey], /) -> FridArray:
        with self:
            return [v for k in keys if (v := await self.aget_frid(k)) is not MISSING]
    async def aput_bulk(self, data: VStorePutBulkData, /, flags) -> int:
        with self:
            count = 0
            for k, v in as_kv_pairs(data):
                if await self.aput_frid(k, v, flags):
                    count += 1
            return count
    async def adel_bulk(self, keys: Iterable[VStoreKey]) -> int:
        with self:
            count = 0
            for k in keys:
                if await self.adel_frid(k):
                    count += 1
            return count
    async def aget_text(self, key: VStoreKey, alt: _T=None) -> str|_T:
        data = await self.aget_frid(key)
        if data is MISSING:
            return alt
        assert isinstance(data, str)
        return data
    async def aget_blob(self, key: VStoreKey, alt: _T=None) -> BlobTypes|_T:
        data = await self.aget_frid(key)
        if data is MISSING:
            return alt
        assert isinstance(data, BlobTypes)
        return data
    async def aget_list(self, key: VStoreKey, sel: VSListSel, alt: _T=None) -> FridArray|_T:
        data = await self.aget_frid(key, sel)
        if data is MISSING:
            return alt
        assert is_frid_array(data)
        return data
    async def aget_dict(self, key: VStoreKey, sel: VSDictSel, alt: _T=None) -> StrKeyMap|_T:
        data = await self.aget_frid(key, sel)
        if data is MISSING:
            return alt
        assert is_frid_skmap(data)
        return data

class AsyncToSyncStoreMixin(ValueStore):
    """This mixin converts the sync value store API to an async one.

    This mixin should only be used to the implementation that are generally
    considered as non-blocking (e.g., in memory or fast disk.)
    Assume there is already a sync version of the class calls MySyncStore
    that implements ValueStore; one can just use
    ```
        class MyAsyncStore(AsyncToSyncValueStoreMixin, MySyncStore):
            pass
    ```
    """
    async def aget_meta(self, keys: Iterable[VStoreKey]) -> Mapping[str,StoreEntryMetaData]:
        return self.get_meta(keys) # pyright: ignore
    async def aget_frid(self, key: VStoreKey, sel: VStoreSel=None) -> FridValue|FridBeing:
        return self.get_frid(key, sel) # pyright: ignore
    async def aput_frid(self, key: VStoreKey, val: FridValue, /, flags) -> int|bool:
        return self.put_frid(key, val, flags) # pyright: ignore
    async def adel_frid(self, key: VStoreKey, sel: VStoreSel=None, /) -> int|bool:
        return self.del_frid(key, sel) # pyright: ignore

class SyncToAsyncStoreMixin(ValueStore):
    """This mixin converts the async value store API to a sync one with asyncio.run().

    Assume there is already a sync version of the class calls MySyncStore
    that implements ValueStore; one can just use
    ```
        class MyAsyncStore(AsyncToSyncValueStoreMixin, MySyncStore):
            pass
    ```
    """
    def get_meta(self, keys: Iterable[VStoreKey]) -> Mapping[str,StoreEntryMetaData]:
        return asyncio.run(self.aget_meta(keys))
    def get_frid(self, key: VStoreKey, sel: VStoreSel=None) -> FridValue|FridBeing:
        return asyncio.run(self.aget_frid(key, sel))
    def put_frid(self, key: VStoreKey, val: FridValue, /, flags) -> int|bool:
        return asyncio.run(self.aput_frid(key, val, flags))
    def del_frid(self, key: VStoreKey, sel: VStoreSel=None, /) -> int|bool:
        return asyncio.run(self.adel_frid(key, sel))

