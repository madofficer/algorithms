n = int(input())
x = int(input()) - 1
y = int(input()) - 1

heap = set()
heap.add(x)
heap.add(y)

def heapify_up(index: int):
    parent_index = (index - 1) // 2

    while parent_index >= 0 and parent_index not in heap:
        heap.add(parent_index)
        index = parent_index
        parent_index = (index - 1) // 2

    if parent_index in heap:
        return parent_index + 1


heapify_up(x)
print(heapify_up(y))
