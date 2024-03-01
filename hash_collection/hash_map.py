from base_hash_collection import BaseHashCollection


class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"KeyValuePair({self.key}, {self.value})"

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value


class HashMap(BaseHashCollection):
    def __setitem__(self, key, value) -> None:
        local_linked_list = self.store[self.storage_index(key)]

        # check if key already in collection -> update value then
        for kv_pair in local_linked_list:
            if kv_pair.key == key:
                kv_pair.value = value
                return

        local_linked_list.append(KeyValuePair(key, value))
        self.num_elements += 1
        self.update_load_factor()

        if self.load_factor >= self.load_factor_threshold:
            self.increase_store_size()

    def __getitem__(self, key):
        local_linked_list = self.store[self.storage_index(key)]

        # check if key already in collection -> update value then
        for kv_pair in local_linked_list:
            if kv_pair.key == key:
                return kv_pair.value

        return None

    def add(self, element: KeyValuePair) -> None:
        self[element.key] = element.value

    def __contains__(self, key) -> bool:
        local_linked_list = self.store[self.storage_index(key)]

        # check if key already in collection -> update value then
        for kv_pair in local_linked_list:
            if kv_pair.key == key:
                return True

        return False

    def remove(self, key) -> None:
        if key not in self:  # nothing to remove
            return

        local_linked_list = self.store[self.storage_index(key)]
        element = KeyValuePair(key, self[key])
        local_linked_list.delete_by_element(element)
        self.num_elements -= 1

    def __repr__(self) -> str:
        return f"HashMap[size={len(self)}, load factor: {self.load_factor}]: {self.store}"


if __name__ == "__main__":
    hashmap = HashMap(max_num_elements=5)
    hashmap["a"] = 2
    hashmap["a"] = 3
    hashmap["b"] = 3
    hashmap["c"] = 3
    hashmap["d"] = 3
    hashmap["e"] = 3
    print(hashmap["a"])
    hashmap["a"] = 4
    print(hashmap["a"])
    hashmap.remove("a")
    print(hashmap)
    print("d" in hashmap)


