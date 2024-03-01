from binary_tree import BinaryNodeTree
from typing import Union


class BinarySearchTree(BinaryNodeTree):
    def __init__(self, value=None):
        super().__init__(value)

    def insert(self, input: Union['BinarySearchTree', int, None]) -> None:
        if isinstance(input, BinarySearchTree):
            value = input.value
        else:
            value = input

        if self.is_leaf() and self.value is None:
            self.value = input
            return

        bst = self
        while bst:
            if value <= bst.value:
                if bst.left is None:
                    bst.left = input  # write into left
                    bst = None
                else:
                    bst = bst.left  # move to left
            else:
                if bst.right is None:
                    bst.right = input  # write into right
                    bst = None
                else:
                    bst = bst.right  # move to right

    def delete(self, value):
        parent, child, is_left_child = self.search_with_parent(value)

        if is_left_child:
            parent.left = None if child.is_leaf() else child.left
            if child.right is not None:
                self.insert(child.right)
        else:
            parent.right = None if child.is_leaf() else child.right
            if child.left is not None:
                self.insert(child.left)

    def search(self, value) -> 'BinarySearchTree':
        _, ptr, _ = self.search_with_parent(value)
        return ptr

    def search_with_parent(self, value) -> tuple['BinarySearchTree', 'BinarySearchTree', bool]:
        parent = None
        ptr = self
        is_left_child = True
        while ptr is not None and ptr.value != value:
            parent = ptr
            if value < ptr.value:
                ptr = ptr.left
                is_left_child = True
            else:
                ptr = ptr.right
                is_left_child = False
        return parent, ptr, is_left_child


def main():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(2)
    bst.insert(5)

    bst2 = BinarySearchTree()
    bst2.insert(15)
    bst2.insert(20)
    bst2.insert(12)

    bst.insert(bst2)

    print(bst)
    print(bst.search(10))
    print(bst.delete(15))
    print(bst)


if __name__ == "__main__":
    main()
