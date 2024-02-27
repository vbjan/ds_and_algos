from linked_list.linked_list import LinkedList


class HashSet:
    def __init__(self, max_num_elements):
        self.max_num_elements = max_num_elements
        self.num_elements = 0
        self.load_factor = 0
        self.load_factor_threshold = 0.7
        self.store = [LinkedList() for _ in range(self.max_num_elements)]

    def add(self, element) -> None:
        local_linked_list = self.store[self.storage_index(element)]
        if element in local_linked_list:  # element already present in HashSet
            return
        local_linked_list.append(element)
        self.num_elements += 1
        self.update_load_factor()
        if self.load_factor >= self.load_factor_threshold:
            self.increase_store_size()

    def __contains__(self, element):
        return element in self.store[self.storage_index(element)]

    def remove(self, element) -> None:
        if element not in self:
            raise AssertionError("Can't remove element from HashSet that is not in HashSet!")
        local_linked_list = self.store[self.storage_index(element)]
        local_linked_list.delete_by_element(element)
        self.num_elements -= 1
        self.update_load_factor()

    def storage_index(self, element) -> int:
        # absolute hash value is mapped to range of possible indices in array
        return abs(hash(element)) % self.max_num_elements

    def update_load_factor(self) -> None:
        self.load_factor = self.num_elements / self.max_num_elements

    def __repr__(self) -> str:
        return f"HashSet: {self.store}, len: {len(self)}, load factor: {self.load_factor}"

    def __len__(self) -> int:
        return self.num_elements

    def increase_store_size(self):
        self.max_num_elements *= 2
        old_store = self.store
        self.store = [LinkedList() for _ in range(self.max_num_elements)]
        self.num_elements = 0
        for linked_list in old_store:
            for element in linked_list:
                self.add(element)
        self.update_load_factor()


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



