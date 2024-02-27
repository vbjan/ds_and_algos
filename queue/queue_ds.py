from abc import ABC
from abc import abstractmethod
from linked_list.linked_list import LinkedList
import warnings


class BaseQueue(ABC):
    @abstractmethod
    def enqueue(self, element) -> None:
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def peek(self):
        pass


class ArrayQueue(BaseQueue):  # Using circular buffer technique
    def __init__(self, max_num_elements):
        self.max_num_elements = max_num_elements
        self.store = [None] * self.max_num_elements
        self.head = self.tail = self.size = 0

    def enqueue(self, element) -> None:
        if self.is_full():
            raise AssertionError(f"Queue of max size {self.max_num_elements} is full.")
        self.store[self.tail] = element
        self.tail = (self.tail + 1) % self.max_num_elements
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            warnings.warn("Tried to dequeue from empty ArrayQueue!")
            return None
        element = self.store[self.head]
        self.store[self.head] = None
        self.head = (self.head + 1) % self.max_num_elements
        self.size -= 1
        return element

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.store[self.head]

    def __repr__(self) -> str:
        return f"ArrayQueue: {self.store}, H: {self.head}, T: {self.tail}, len: {len(self)}"

    def __len__(self) -> int:
        return self.size

    def is_full(self) -> bool:
        return self.size == self.max_num_elements

    def is_empty(self) -> bool:
        return self.size == 0


class LinkedListQueue(BaseQueue):
    def __init__(self):
        self.store = LinkedList()

    def enqueue(self, element) -> None:  # O(1)
        self.store.append(element)

    def dequeue(self):  # O(1)
        return self.store.pop_head()

    def peek(self):  # O(1)
        return self.store[0]

    def __repr__(self) -> str:
        return f"LinkedListQueue: {self.store}"


if __name__ == "__main__":
    q = ArrayQueue(max_num_elements=5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)
    q.dequeue()
    print(q)
    q.dequeue()
    print(q)
    q.dequeue()
    print(q)
    q.dequeue()
    print(q)
    q.enqueue(4)
    print(q)
    q.enqueue(5)
    print(q)
    q.enqueue(6)
    print(q)
    q.enqueue(7)
    q.enqueue(8)

    print(q)
    print(q.dequeue())
    print(q)
    print(q.peek())
