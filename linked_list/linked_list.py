from typing import Optional


class Node:
    def __init__(self, element):
        self.element = element
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        return f"Node({self.element})->"


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.size: int = 0
        self.tail: Optional[Node] = None
        self.iter_index: int = 0

    def append(self, element) -> None:  # O(1)
        new_node = Node(element)
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

    def index_is_allowed(self, i: int) -> bool:
        return 0 <= i <= self.size

    def insert(self, element, i: int) -> None:
        if not self.index_is_allowed(i):
            raise IndexError("Index out of bounds.")

        new_node = Node(element)
        if i == 0:  # no previous element, O(1)
            new_node.next = self.head
            self.head = new_node
            self.size += 1
        elif i == self.size:  # inserting at last element = appending, O(1)
            self.append(element)
        else:  # O(n) because of traversing through list
            prev_node = self[i-1]
            temp = prev_node.next
            prev_node.next = new_node
            new_node.next = temp
            self.size += 1

    def delete_by_index(self, i: int) -> None:
        if not self.index_is_allowed(i):
            raise IndexError("Index out of bounds.")
        if i == 0:  # no previous element, O(1)
            self.head = self.head.next
            self.size -= 1
        else:
            prev_node = self[i-1]
            if i == self.size - 1:  # deleted last element, need to relocated tail pointer
                self.tail = prev_node
            prev_node.next = prev_node.next.next
            self.size -= 1

    def delete_by_element(self, element) -> None:
        steps = 0
        prev_node, node = None, self.head
        while node.element != element:
            prev_node = node
            node = node.next
            steps += 1
            if node == self.tail:
                raise Warning(f"Tried to delete {element} which is not in LinkedList!")
        if len(self) == 1:
            self.__init__()
        else:
            prev_node.next = node.next

    def pop_head(self) -> Node:  # O(1)
        if self.is_empty():
            raise IndexError("Attempted to pop head of empty LinkedList.")
        node = self.head
        self.head = self.head.next
        self.size -= 1
        return node

    def pop_tail(self) -> Node:  # O(n)
        node = self.tail
        self.tail = self[self.size - 2]
        self.tail.next = None
        return node

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter_index < len(self):
            node = self[self.iter_index]
            self.iter_index += 1
            return node.element
        else:
            raise StopIteration

    def __contains__(self, element) -> bool:  # O(n)
        ptr = self.head
        while ptr:
            if ptr.element == element: return True
            ptr = ptr.next
        return False

    def __len__(self):
        return self.size

    def __repr__(self) -> str:  # O(n)
        node, node_names = self.head, []
        while node:
            node_name = f"Head{str(node)}" if node is self.head else f"Tail{str(node)}" if node is self.tail else str(node)
            node_names.append(node_name)
            node = node.next
        return f"LinkedList[size={self.size}]: {''.join(node_names)}None"


if __name__ == "__main__":
    l = LinkedList()
    l.append(2)
    l.append(3)
    l.append(1)
    print(l)
    print(l[1])
    print(l[2])
    l.insert(10, 3)
    print(l)
    l.insert(11, 0)
    print(l)
    print(0 in l)
    # prints out LinkedList[size=5]: HeadNode(11)->Node(2)->Node(3)->Node(10)->TailNode(1)->None

    for ele in l:
        print(ele)

    l.delete_by_element(2)
    print(l)
    l.pop_head()
    print(l)
    l.delete_by_element(2)
    print(l)
    l.pop_tail()
    print(l)