# Heap
*Specialized tree data structure to store collection and dynamically allow efficient retrieval of the min or max.*

- Allows for adding and removing of elements, while keeping the heap property, in $O(log n)$
- Usually based on array implementation of tree
- Allows for efficient implementation of priority queues!

**Adding element**: Elements are added as leaves and then bubbled up until the heap property is fulfilled again

**Removing the root**: Swap the root with last added element and then bubble this element down


