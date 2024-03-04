from heap.heap import Heap
from queue_ds import BaseQueue
import math
from typing import Any, Tuple


class PriorityQueue(BaseQueue):
    def __init__(self, max_num_elements):
        self.max_num_elements = max_num_elements
        self.heap = Heap(depth=int(math.log(self.max_num_elements, 2)), sorting_func="max")

    def enqueue(self, element, *args, **kwargs) -> None:  # O(1)
        priority_value = kwargs.get('priority_value')
        if priority_value is None:
            raise ValueError("priority_value is required")
        if not isinstance(priority_value, int):
            raise TypeError("priority_value must be an int")
        self.heap.add(element=element, value=priority_value)

    def dequeue(self) -> Tuple[Any, int]:  # O(1)
        return self.heap.pop_root()

    def peek(self) -> Tuple[Any, int]:  # O(1)
        return self.heap[0].element, self.heap[0].value

    def __repr__(self) -> str:
        return f"PriorityQueue: {self.heap}"


if __name__ == "__main__":
    p_queue = PriorityQueue(max_num_elements=100)
    p_queue.enqueue(element="JP", priority_value=2)
    p_queue.enqueue(element="L", priority_value=1)
    p_queue.enqueue(element="R", priority_value=6)
    p_queue.enqueue(element="D", priority_value=-1)
    print(p_queue)
    print(p_queue.dequeue())
    print(p_queue.dequeue())
    print(p_queue.peek())