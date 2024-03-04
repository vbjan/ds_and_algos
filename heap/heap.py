from tree.tree import ArrayTree
from typing import Literal


class Heap(ArrayTree):

    SORTING_FUNCS = {
        "min": min,
        "max": max
    }

    def __init__(self, depth: int, sorting_func: Literal["min", "max"]):
        super().__init__(max_children=2, depth=depth)
        self.num_elements = 0
        assert sorting_func in self.SORTING_FUNCS.keys()
        self.sorting_func = self.SORTING_FUNCS[sorting_func]

    @property
    def last_element(self):
        return self.store[self.num_elements - 1]

    @last_element.setter
    def last_element(self, value) -> None:
        self.store[self.num_elements - 1] = value

    def add(self, value) -> None:
        if self.num_elements == 0:
            self.set_root(value)
            self.num_elements += 1
            return

        # add new value as leaf to heap
        self.store[self.num_elements] = value

        # bubble leaf up
        child_idx, child_value = self.num_elements, value
        parent_idx = self.parent_idx(child_idx)
        parent_value = self.store[parent_idx]

        while parent_idx >= 0 and parent_value != self.sorting_func(parent_value, child_value):
            # swap values
            self.store[parent_idx], self.store[child_idx] = child_value, parent_value

            # move up one level in heap
            parent_idx, child_idx = self.parent_idx(parent_idx), parent_idx
            parent_value, child_value = self.store[parent_idx], self.store[child_idx]

        self.num_elements += 1

    def parent_idx(self, child_idx: int) -> int:
        return (child_idx - 1) // self.max_children

    def remove_root(self):
        root_val = self[0]

        # swap last added element into root and bubble it down
        self.store[0], self.last_element = self.last_element, None

        # bubble root down
        curr_val, curr_idx = self.store[0], 0
        children_vals = self.store[1:min(self.max_children + 1, self.num_elements - 1)]

        while not all(ele is None for ele in children_vals) and curr_val != self.sorting_func(curr_val, *children_vals):
            # swap the parent value with child value according to sorting function
            child_idx = self.max_children * curr_idx + 1 + self.sorting_func(enumerate(children_vals), key=lambda x: x[1])[0]
            self.store[curr_idx], self.store[child_idx] = self.store[child_idx], curr_val

            # move into one level lower in heap
            curr_idx = child_idx
            curr_val = self.store[child_idx]
            children_vals = self.store[self.max_children * curr_idx + 1:min(self.max_children * curr_idx + 3, self.num_elements - 1)]

        self.num_elements -= 1
        return root_val

    def read_root(self):
        return self[0]


if __name__ == "__main__":
    heap = Heap(depth=4, sorting_func='max')
    heap.add(1)
    heap.add(-1)
    heap.add(2)
    heap.add(0)
    heap.add(-2)
    heap.add(10)
    print(heap)
    mins = []
    mins.append(heap.remove_root())
    mins.append(heap.remove_root())
    #heap.add(-2)
    #heap.add(10)
    print(mins)
    print(heap)


