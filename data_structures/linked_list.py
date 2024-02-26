from typing import Optional


class Node:
    def __init__(self, element: int):
        self.element: int = element
        self.next: Optional[Node, None] = None

    def __repr__(self):
        return f"Node({self.element})->"


class LinkedList:
    def __init__(self):
        self.head: Optional[Node, None] = None
        self.size: int = 0
        self.tail: Optional[Node, None] = None

    def append(self, new_node: Node) -> None:  # O(1)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.size += 1

    def __getitem__(self, item: int) -> Node:  # O(n)
        if self.is_empty():
            raise AssertionError("LinkedList is empty.")
        if not self.index_is_allowed(item):
            raise IndexError("Index out of bounds.")
        steps, node = 0, self.head
        while steps < item:
            node = node.next
            steps += 1
        return node

    def is_empty(self) -> bool:
        return self.size == 0

    def index_is_allowed(self, i):
        return 0 <= i <= self.size - 1

    def insert(self, new_node: Node, i: int) -> None:
        if not self.index_is_allowed(i):
            raise IndexError("Index out of bounds.")

        if i == 0:  # no previous element, O(1)
            new_node.next = self.head
            self.head = new_node
            self.size += 1
        else:  # O(n) because of traversing through list
            prev_node = self[i-1]
            temp = prev_node.next
            prev_node.next = new_node
            new_node.next = temp
            self.size += 1

    def __repr__(self) -> str:  # O(n)
        node, name = self.head, ""
        while node:
            if node is self.head:
                name += f"Head{str(node)}"
            elif node is self.tail:
                name += f"Tail{str(node)}"
            else:
                name += str(node)
            node = node.next
        return f"LinkedList[size={self.size}]: {name}None"


if __name__ == "__main__":
    list = LinkedList()
    list.append(Node(2))
    list.append(Node(3))
    list.append(Node(1))
    print(list)
    print(list[1])
    print(list[2])
    list.insert(Node(10), 2)
    print(list)
    list.insert(Node(11), 0)
    print(list)
    # prints out LinkedList[size=5]: HeadNode(11)->Node(2)->Node(3)->Node(10)->TailNode(1)->None
