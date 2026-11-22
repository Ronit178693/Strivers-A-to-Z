class BaseHeap:
    """
    A foundational parent class handling the universal complete binary tree
    mechanics, size Tracking, and array index lookups.
    """
    def __init__(self, array=None):
        self.heap = [] if array is None else list(array)
        if self.heap:
            self._build_heap()

    def size(self):
        """Returns the total number of elements currently stored in the heap."""
        return len(self.heap)

    def is_empty(self):
        """Returns True if the heap contains no elements."""
        return len(self.heap) == 0

    def _get_parent(self, i):
        return (i - 1) // 2

    def _get_left_child(self, i):
        return 2 * i + 1

    def _get_right_child(self, i):
        return 2 * i + 2

    def _compare(self, parent_idx, child_idx):
        """Must be overridden by child classes to determine Min vs Max logic."""
        raise NotImplementedError

    def _sift_up(self, i):
        """Moves an element up toward the root to heal a priority violation."""
        while i > 0:
            parent = self._get_parent(i)
            if self._compare(i, parent):
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def _sift_down(self, i):
        """Moves an element down toward the leaves to heal a priority violation."""
        n = len(self.heap)
        while True:
            target = i
            left = self._get_left_child(i)
            right = self._get_right_child(i)

            if left < n and self._compare(left, target):
                target = left
            if right < n and self._compare(right, target):
                target = right

            if target == i:
                break

            self.heap[i], self.heap[target] = self.heap[target], self.heap[i]
            i = target

    def _build_heap(self):
        """Converts an unsorted array into a valid structured heap in O(n) time."""
        n = len(self.heap)
        start_idx = (n // 2) - 1
        for i in range(start_idx, -1, -1):
            self._sift_down(i)

    def insert(self, item):
        """Inserts a new value into the heap. Complexity: O(log n)"""
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)

    def remove_root(self):
        """Removes and returns the priority root element. Complexity: O(log n)"""
        if self.is_empty():
            raise IndexError("Cannot remove an element from an empty heap.")
        
        if len(self.heap) == 1:
            return self.heap.pop()
            
        root_val = self.heap[0]
        # Swap the tail element into the root slot and force it down
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root_val

    def __str__(self):
        return str(self.heap)