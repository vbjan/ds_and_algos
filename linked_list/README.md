# Linked List
1. **Singly Linked List**: In a singly linked list, each node contains a data element and a pointer/reference to the next node in the sequence. The last node typically points to NULL to indicate the end of the list.
    
2. **Doubly Linked List**: In a doubly linked list, each node contains both a data element and two pointers/references: one to the next node and one to the previous node. This allows traversal of the list in both forward and backward directions.

![Linkedlist](https://github.com/vbjan/ds_and_algos/assets/62449932/004c8d4f-a31f-446a-9c12-c45a4cae6d65)

## Time Complexities
- Access: $O(N)$
- Insertion/Deletion beginning and end: $O(1)$
- Insertion/Deletion beginning at middle: $O(N)$
- Access/Update by Index: O(N)

## Advantages:
- Dynamic size: Linked lists can dynamically grow or shrink in size, unlike arrays with fixed sizes.
- Efficient insertion and deletion: Insertion and deletion of elements can be done efficiently, especially when compared to arrays, as it only requires changing pointers.
- No memory wastage: Linked lists only use memory that is needed for the elements they contain.

## Disadvantages
- Lack of random access: Unlike arrays, accessing elements in a linked list requires traversal from the beginning of the list, making random access inefficient.
- Additional memory overhead: Linked lists require additional memory for storing pointers/references, increasing memory overhead compared to arrays.
- More complex implementation: Implementing operations like traversal, insertion, and deletion in linked lists may require more complex code compared to arrays.
