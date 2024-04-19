from __future__ import annotations

from collections import defaultdict
from typing import TypeVar, Generic, Dict, Optional, Iterable, List, Iterator, Tuple, Generator, Union
from .parents import OuterProxy

T = TypeVar('T', bound=OuterProxy)


class Collection(Generic[T]):
    __is_collection__ = True

    _data: List[T]

    _indexed_values: Dict[str, set]
    _indexed_to_objects: Dict[any, list]

    shallow_list = property(fget=lambda self: self.data)

    def __init__(
            self,
            data: Optional[Iterable[T]] = None,
            sync_on_append: Dict[str, Collection] = None,
            contain_given_in_attribute: Dict[str, Collection] = None,
            contain_attribute_in_given: Dict[str, Collection] = None,
            append_object_to_attribute: Dict[str, T] = None
    ) -> None:
        self._contains_ids = set()
        self._data = []

        self.parents: List[Collection[T]] = []
        self.children: List[Collection[T]] = []

        # List of collection attributes that should be modified on append
        # Key: collection attribute (str) of appended element
        # Value: main collection to sync to
        self.contain_given_in_attribute: Dict[str, Collection] = contain_given_in_attribute or {}
        self.append_object_to_attribute: Dict[str, T] = append_object_to_attribute or {}
        self.sync_on_append: Dict[str, Collection] = sync_on_append or {}

        self._id_to_index_values: Dict[int, set] = defaultdict(set)
        self._indexed_values = defaultdict(lambda: None)
        self._indexed_to_objects = defaultdict(lambda: None)

        self.extend(data)

    def _map_element(self, __object: T, from_map: bool = False):
        self._contains_ids.add(__object.id)

        for name, value in (*__object.indexing_values, ('id', __object.id)):
            if value is None or value == __object._inner._default_values.get(name):
                continue

            self._indexed_values[name] = value
            self._indexed_to_objects[value] = __object

            self._id_to_index_values[__object.id].add((name, value))

    def _unmap_element(self, __object: Union[T, int]):
        obj_id = __object.id if isinstance(__object, OuterProxy) else __object

        if obj_id in self._contains_ids:
            self._contains_ids.remove(obj_id)

        for name, value in self._id_to_index_values[obj_id]:
            if name in self._indexed_values:
                del self._indexed_values[name]
            if value in self._indexed_to_objects:
                del self._indexed_to_objects[value]

        del self._id_to_index_values[obj_id]

    def _contained_in_self(self, __object: T) -> bool:
        if __object.id in self._contains_ids:
            return True

        for name, value in __object.indexing_values:
            if value is None:
                continue
            if value == self._indexed_values[name]:
                return True
        return False

    def _contained_in_sub(self, __object: T, break_at_first: bool = True) -> List[Collection]:
        """
        Gets the collection this object is found in, if it is found in any.

        :param __object:
        :param break_at_first:
        :return:
        """
        results = []

        if self._contained_in_self(__object):
            return [self]

        for collection in self.children:
            results.extend(collection._contained_in_sub(__object, break_at_first=break_at_first))

            if break_at_first:
                return results

        return results

    def _get_root_collections(self) -> List[Collection]:
        if not len(self.parents):
            return [self]

        root_collections = []
        for upper_collection in self.parents:
            root_collections.extend(upper_collection._get_root_collections())
        return root_collections

    @property
    def _is_root(self) -> bool:
        return len(self.parents) <= 0

    def _get_parents_of_multiple_contained_children(self, __object: T):
        results = []
        if len(self.children) < 2 or self._contained_in_self(__object):
            return results

        count = 0

        for collection in self.children:
            sub_results = collection._get_parents_of_multiple_contained_children(__object)

            if len(sub_results) > 0:
                count += 1
                results.extend(sub_results)

        if count >= 2:
            results.append(self)

        return results

    def merge_into_self(self, __object: T, from_map: bool = False):
        """
        1. find existing objects
        2. merge into existing object
        3. remap existing object
        """
        if __object.id in self._contains_ids:
            return

        existing_object: T = None

        for name, value in __object.indexing_values:
            if value is None:
                continue

            if value == self._indexed_values[name]:
                existing_object = self._indexed_to_objects[value]
                if existing_object.id == __object.id:
                    return None

                break

        if existing_object is None:
            return None

        existing_object.merge(__object)

        # just a check if it really worked
        if existing_object.id != __object.id:
            raise ValueError("This should NEVER happen. Merging doesn't work.")

        self._map_element(existing_object, from_map=from_map)

    def contains(self, __object: T) -> bool:
        return len(self._contained_in_sub(__object)) > 0

    def _find_object_in_self(self, __object: T) -> Optional[T]:
        for name, value in __object.indexing_values:
            if value == self._indexed_values[name]:
                return self._indexed_to_objects[value]

    def _find_object(self, __object: T, no_sibling: bool = False) -> Tuple[Collection[T], Optional[T]]:
        other_object = self._find_object_in_self(__object)
        if other_object is not None:
            return self, other_object

        for c in self.children:
            o, other_object = c._find_object(__object)
            if other_object is not None:
                return o, other_object

        if no_sibling:
            return self, None

        """
        # find in siblings and all children of siblings
        for parent in self.parents:
            for sibling in parent.children:
                if sibling is self:
                    continue

                o, other_object = sibling._find_object(__object, no_sibling=True)
                if other_object is not None:
                    return o, other_object
        """

        return self, None

    def append(self, __object: Optional[T], already_is_parent: bool = False, from_map: bool = False):
        """
        If an object, that represents the same entity exists in a relevant collection,
        merge into this object. (and remap)
        Else append to this collection.

        :param __object:
        :param already_is_parent:
        :param from_map:
        :return:
        """

        if __object is None:
            return

        append_to, existing_object = self._find_object(__object)

        if existing_object is None:
            # append
            append_to._data.append(__object)
            append_to._map_element(__object)

            # only modify collections if the object actually has been appended
            for collection_attribute, child_collection in self.contain_given_in_attribute.items():
                __object.__getattribute__(collection_attribute).contain_collection_inside(child_collection, __object)

            for attribute, new_object in self.append_object_to_attribute.items():
                __object.__getattribute__(attribute).append(new_object)
            
            for attribute, collection in self.sync_on_append.items():
                collection.extend(__object.__getattribute__(attribute))
                __object.__setattr__(attribute, collection)

        else:
            # merge only if the two objects are not the same
            if existing_object.id == __object.id:
                return

            old_id = existing_object.id

            existing_object.merge(__object)

            if existing_object.id != old_id:
                append_to._unmap_element(old_id)

            append_to._map_element(existing_object)

    def extend(self, __iterable: Optional[Generator[T, None, None]]):
        if __iterable is None:
            return

        for __object in __iterable:
            self.append(__object)

    def contain_collection_inside(self, sub_collection: Collection, _object: T):
        """
        This collection will ALWAYS contain everything from the passed in collection
        """
        if self is sub_collection or sub_collection in self.children:
            return

        _object._inner._is_collection_child[self] = sub_collection
        _object._inner._is_collection_parent[sub_collection] = self

        self.children.append(sub_collection)
        sub_collection.parents.append(self)

    @property
    def data(self) -> List[T]:
        return list(self.__iter__())

    def __len__(self) -> int:
        return len(self._data) + sum(len(collection) for collection in self.children)

    @property
    def empty(self) -> bool:
        return self.__len__() <= 0

    def __iter__(self, finished_ids: set = None) -> Iterator[T]:
        _finished_ids = finished_ids or set()

        for element in self._data:
            if element.id in _finished_ids:
                continue
            _finished_ids.add(element.id)
            yield element

        for c in self.children:
            yield from c.__iter__(finished_ids=finished_ids)

    def __merge__(self, __other: Collection, override: bool = False):
        self.extend(__other)

    def __getitem__(self, item: int):
        if item < len(self._data):
            return self._data[item]

        item = item - len(self._data)

        for c in self.children:
            if item < len(c):
                return c.__getitem__(item)
            item = item - len(c._data)

        raise IndexError
