from abc import ABC, abstractmethod
from linked_list.linked_list import LinkedList


class BaseTree(ABC):
    @abstractmethod
    def __repr__(self) -> str:
        pass


class NodeTree(BaseTree):

    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self) -> str:
        return f"Node(val={self.value}, children={self.children}"

    @classmethod
    def create_child(cls, value) -> 'NodeTree':
        return cls(value)

    def add_child(self, value) -> 'NodeTree':
        child = self.create_child(value)
        self.children.append(child)
        return self

    def __getitem__(self, i):
        return self.children[i]

    def is_leaf(self) -> bool:
        return len(self.children) == 0


class ArrayTree(BaseTree):
    def __init__(self, max_children, depth):
        self.max_children = max_children
        self.depth = depth
        self.num_nodes = sum(self.max_children ** i for i in range(0, self.depth))
        self.store = [None] * self.num_nodes

    def __repr__(self) -> str:
        return f"ArrayTree( \n" \
               f"   max_children={self.max_children}, \n" \
               f"   depth={self.depth},\n" \
               f"   store={self.store}" \
               f"\n)"

    def __getitem__(self, indcs):
        if isinstance(indcs, tuple):
            ptr = i = 0
            for i in indcs:
                assert self.store[ptr]
                ptr *= self.max_children
                ptr += i
            return self.store[i]
        else:
            return self.store[indcs]

    def __setitem__(self, indcs, value):
        if isinstance(indcs, int):
            if indcs < 0 or self.max_children - 1 < indcs:
                raise IndexError(f"Index {indcs} exceeds allowed range [0, {self.max_children-1}]!")
            self.store[indcs + 1] = value

        else:
            if len(indcs) >= self.depth:
                raise IndexError(f"Number of indices exceeds depth={self.depth} of tree!")

            ptr = 0
            for depth, i in enumerate(indcs):
                if i < 0 or self.max_children - 1 < i:
                    raise IndexError(f"Index {i} exceeds allowed range [0, {self.max_children - 1}]!")

                ptr = ptr * self.max_children + i + 1

                # make sure that we are actually moving to an existing child
                if depth != len(indcs) - 1 and self.store[ptr] is None:
                    raise AssertionError("Tried to assign value to node that does not have parent!")

            self.store[ptr] = value

    def set_root(self, value):
        self.store[0] = value


class LinkedListTree(BaseTree):
    def __init__(self, value):
        self.value = value
        self.children = LinkedList()

    def add_child(self, value) -> None:
        child = self.create_child(value)
        self.children.append(child)

    @classmethod
    def create_child(cls, value) -> 'LinkedListTree':
        return cls(value)

    def __repr__(self) -> str:
        return f"LinkedListTree[value={self.value}], children: {self.children}"

    def __getitem__(self, indcs) -> 'LinkedListTree':
        if isinstance(indcs, int):
            return self.children[indcs].element

        else:
            child = None
            children = self.children

            for i in indcs:
                child = children[i].element
                children = child.children

            return child


if __name__ == "__main__":
    # LinkedListTree
    tree0 = LinkedListTree(0)
    tree0.add_child(1)
    tree0.add_child(2)
    tree0[0].add_child(10)
    print(tree0)
    print(tree0[0, 0])
    print(tree0[1])
    exit()

    # ArrayTree
    tree = ArrayTree(max_children=3, depth=4)
    tree.set_root(0)
    tree[0] = 1
    print(tree)
    tree[0, 2] = 1
    print(tree)
    tree[0, 2, 0] = 1
    print(tree)
    exit()

    # NodeTree
    tree = NodeTree(1)
    tree.add_child(2)
    tree.add_child(3)
    tree[0].add_child(1)
    tree[1].add_child(2)
    print(tree)