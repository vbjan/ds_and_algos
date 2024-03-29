from base_hash_collection import BaseHashCollection
from copy import deepcopy


class HashSet(BaseHashCollection):

    def __contains__(self, element):
        return element in self.store[self.storage_index(element)]

    def add(self, element) -> None:
        idx = self.storage_index(element)
        local_linked_list = self.store[idx]
        if element in local_linked_list:  # element already present in HashSet
            return

        local_linked_list.append(element)
        self.num_elements += 1
        self.update_load_factor()

        if self.load_factor >= self.load_factor_threshold:
            self.increase_store_size()

    def remove(self, element) -> None:
        if element not in self:  # nothing to remove
            return

        local_linked_list = self.store[self.storage_index(element)]
        local_linked_list.delete_by_element(element)
        self.num_elements -= 1
        self.update_load_factor()

    def __repr__(self) -> str:
        return f"HashSet: {self.store}, len: {len(self)}, load factor: {self.load_factor}"

    def intersect(self, other: 'HashSet') -> 'HashSet':
        smaller_set = other if len(other) < len(self) else self
        larger_set = self if len(other) < len(self) else other
        result_set = HashSet(len(smaller_set))

        for linked_list in smaller_set.store:
            for element in linked_list:
                if element in larger_set:
                    result_set.add(element)

        return result_set

    def union(self, other: 'HashSet') -> 'HashSet':
        smaller_set = other if len(other) < len(self) else self
        larger_set = self if len(other) < len(self) else other
        result_set = deepcopy(larger_set)

        for linked_list in smaller_set.store:
            for element in linked_list:
                result_set.add(element)

        return result_set


if __name__ == "__main__":
    test_set = HashSet(max_num_elements=2)
    print(test_set)
    test_set.add("one")
    print(test_set)
    test_set.add("two")
    print(test_set)
    test_set.add("three")
    print(test_set)
    print("two" in test_set)
    print(3 in test_set)
    print(None in test_set)
    test_set.remove("two")
    print(test_set)

    test_set_2 = HashSet(max_num_elements=2)
    test_set_2.add("one")
    print(test_set_2)

    print(test_set_2.union(test_set))



