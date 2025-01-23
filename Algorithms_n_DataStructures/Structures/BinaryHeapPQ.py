class BinaryHeap:
    def __init__(self):
        self.heap = []

    def __str__(self):
        return str(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while parent_index >= 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index
            parent_index = (index - 1) // 2

    def get_min(self):
        if self.is_empty():
            raise IndexError('No root in empty heap')
        else:
            return self.heap[0]

    def poll(self):
        if self.is_empty():
            raise IndexError('No root in empty heap')
        else:
            min_val = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self._heapify_down(0)
        return min_val

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

if __name__ == "__main__":

    heap = BinaryHeap()
    print(heap.is_empty())

    heap.insert(8)
    heap.insert(4)
    heap.insert(9)
    heap.insert(17)
    heap.insert(12)
    print(heap.get_min())
    print(heap)
    heap.insert(1)
    heap.insert(10)
    print(heap)
    print(heap.poll())
    print(heap)

