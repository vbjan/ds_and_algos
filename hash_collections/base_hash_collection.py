from abc import ABC
from abc import abstractmethod
from linked_list.linked_list import LinkedList


class BaseHashCollection(ABC):
    def __init__(self, max_num_elements):
        self.max_num_elements = max_num_elements
        self.num_elements = 0
        self.load_factor = 0
        self.load_factor_threshold = 0.7
        self.store = [LinkedList() for _ in range(self.max_num_elements)]

    def __len__(self) -> int:
        return self.num_elements

    def storage_index(self, element) -> int:
        # absolute hash value is mapped to range of possible indices in array
        return abs(hash(element)) % self.max_num_elements

    def update_load_factor(self) -> None:
        self.load_factor = self.num_elements / self.max_num_elements

    @abstractmethod
    def add(self, element) -> None:
        pass

    def increase_store_size(self):
        self.max_num_elements *= 2
        old_store = self.store
        self.store = [LinkedList() for _ in range(self.max_num_elements)]
        self.num_elements = 0  # need to set to zero because add method counts added elements

        for linked_list in old_store:
            for element in linked_list:
                self.add(element)

        self.update_load_factor()
