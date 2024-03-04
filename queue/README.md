# Queue

# Basics
*First in first out: FIFO*
- Used in BFS algorithm!
- Used for sliding window problems
- Implementation based on linked list and array in [`queue_ds.py`](./queue_ds.py)

![Queue](https://github.com/vbjan/ds_and_algos/assets/62449932/ee229ddf-ae81-4dd9-a285-9c26c8821125)

**Operations:**
1. Enqueue: Add object at end of queue $O(1)$
2. Dequeue: Remove object from end of queue $O(1)$
3. Peek: Look at first element/object of queue

# Priority Queue
Each element in the queue has a corresponding priority value. The elements are dequeued from the priority queue in order of the priority.

Efficient enqueuing in $O(log n)$ and dequeuing in $O(log n)$ requires to store the elements in order with a heap. Find the implementation in [`priority_queue.py`](priority_queue.py).