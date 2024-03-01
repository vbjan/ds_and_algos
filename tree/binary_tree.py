from tree import NodeTree, ArrayTree, LinkedListTree
from typing import Optional


class BinaryNodeTree(NodeTree):
    def __init__(self, value=None):
        super().__init__(value)
        self.children = [None] * 2

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None

    @property
    def left(self) -> Optional['BinaryNodeTree']:
        return self.children[0]

    @left.setter
    def left(self, value):
        if isinstance(value, BinaryNodeTree) or value is None:
            self.children[0] = value
        else:
            self.children[0] = self.create_child(value)

    @property
    def right(self) -> Optional['BinaryNodeTree']:
        return self.children[1]

    @right.setter
    def right(self, value):
        if isinstance(value, BinaryNodeTree) or value is None:
            self.children[1] = value
        else:
            self.children[1] = self.create_child(value)

    def add_child(self, value) -> 'BinaryNodeTree':
        if self.left is None:
            self.left = value
        elif self.right is None:
            self.right = value
        else:
            raise AssertionError("Tried to add child to parent with two children already!")
        return self


class BinaryArrayTree(ArrayTree):
    def __init__(self, depth):
        super().__init__(max_children=2, depth=depth)


if __name__ == "__main__":
    tree = BinaryNodeTree(1)
    tree.right = 1
    tree.left = 2
    print(tree)
    tree.left.add_child(2)
    print(tree)
    print(tree.left)
    print(tree.right)

    tree2 = BinaryArrayTree(depth=3)
    tree2.set_root(1)
    tree2[0] = 2
    tree2[1] = 3
    tree2[0, 0] = 1
    tree2[1, 1] = 2
    print(tree2)
