# Implementing Data Structures from Scratch

This repo is the product of me revisiting and implementing common data structures.
The figure below shows a dependency graph of the different implementations.

<p align="center">
    <img src="https://github.com/vbjan/ds_and_algos/assets/62449932/5f31d3f3-a217-48db-9e84-ef638600bdac" alt="Description of Image" width=65%>
</p>

## Find the Following Implementations:
- `LinkedList` in [`linked_list/linked_list.py`](linked_list/linked_list.py)
- `Stack` in [`stack/stack.py`](stack/stack.py) based on 
  - Array
  - Linked list
- `Queue` in [`queue/queue_ds.py`](queue/queue_ds.py) based on 
  - Array
  - Linked list
- `HashSet` in [`hash_collection/hash_set.py`](hash_collection/hash_set.py`) based on
  - Array and chaining using linked lists
- `HashMap` in [`hash_collection/hash_set.py`](hash_collection/hash_set.py`) based on
  - Array and chaining using linked lists
- `Tree` in [`tree/tree.py`](tree/tree.py) based on
  - Nodes connected using references
  - Array (e.g. for heap)
  - Collecting children of parent in linked list
- `BinaryTree` as subclasses of the tree implementations in [`tree/binary_tree.py`](tree/binary_tree.py) 
- `BinarySearchTree` as subclass of the node based binary tree implementations in [`tree/binary_search_tree.py`](tree/binary_search_tree.py) 
- `Heap` based on array-based implementation of binary tree in [`heap/heap.py`](heap/heap.py)


