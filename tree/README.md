# Tree
A tree is a widely used hierarchical data structure that organizes elements in a hierarchical manner. It is composed of nodes where each node stores a value and can have zero or more child nodes.

![Treedatastructure](https://github.com/vbjan/ds_and_algos/assets/62449932/fb6ec625-3147-457c-bdf4-2c24f018bbca)

The abstract tree data structure can be implemented based on an array, a graph or a collection of linked lists. The different implementations can be found in [`tree.py`](./tree.py).

## Special Versions
- Binary Tree: Only two children for each node, see [`binary_tree.py`](./binary_tree.py).
- Binary Search Tree (BST): Binary tree that allows for efficient searching, deleting and inserting of elements in order, see [`binary_search_tree.py`](./binary_search_tree.py).
  - **Balanced search tree:** structured in such a way that the height differences between the left and right subtrees of any node in the tree are minimal. -> The depth of the tree should be around $O(log N)$. 
  - Search, insert and delete have time complexity  $O(log N)$ for a balanced BST.
- Trie (Prefix Tree)
- Heap