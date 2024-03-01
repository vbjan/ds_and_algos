from tree import NodeTree, ArrayTree, LinkedListTree


class BinaryNodeTree(NodeTree):
    def __init__(self, value):
        super().__init__(value)
        self.left = None
        self.right = None

    def add_child(self, value):
        if len(self.children) == 2:
            raise AssertionError("Tried to add child to node with two children!")
        super().add_child(value)
        if len(self.children) == 1:
            self.left = self.children[0]
        elif len(self.children) == 2:
            self.right = self.children[1]
        else:
            raise AssertionError


class BinaryArrayTree(ArrayTree):
    def __init__(self, depth):
        super().__init__(max_children=2, depth=depth)


if __name__ == "__main__":
    tree = BinaryNodeTree(1)
    tree.add_child(2)
    tree.add_child(3)
    tree.left.add_child(1)
    tree.right.add_child(2)

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
