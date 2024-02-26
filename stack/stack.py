from abc import ABC, abstractmethod
from linked_list.linked_list import LinkedList


class BaseStack(ABC):
    @abstractmethod
    def push(self, element) -> None:
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass


class ArrayStack(BaseStack):
    def __init__(self):
        self.store = []

    def push(self, element):
        self.store.append(element)

    def pop(self):
        if self.is_empty():
            return None

        return self.store.pop()

    def peek(self):
        if self.is_empty():
            return None

        return self.store[-1]

    def is_empty(self) -> bool:
        return len(self.store) == 0

    def __repr__(self):
        return f"ArrayStack: {str(self.store)}"


class LinkedListStack(BaseStack):
    def __init__(self):
        self.store = LinkedList()

    def push(self, element):
        self.store.insert(element, 0)

    def pop(self):
        if self.is_empty():
            return None

        node = self.store.pop_head()
        return node.element

    def peek(self):
        if self.is_empty():
            return None

        return self.store.head.element

    def is_empty(self) -> bool:
        return self.store.is_empty()

    def __repr__(self):
        return f"LinkedListStack: {str(self.store)}"


if __name__ == "__main__":
    stack = LinkedListStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack)
    print(stack.pop())
    print(stack.pop())
    print(stack)
    print(stack.peek())