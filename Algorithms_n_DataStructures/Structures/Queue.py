from Stack import Stack

class Queue(Stack):

    def __init__(self):
        super().__init__()

    def equeue(self, data):
        self.insert_at_end(data)

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Nothing to dequeue from empty queue')
        else:
            return self.pop()

    def front(self):
        if self.is_empty():
            raise IndexError('Nothing front in empty queue')
        return self.peek()


if __name__ == "__main__":
    q = Queue()
    print(q)
    q.equeue(5)
    q.equeue(6)
    print(q)
    print(len(q))
    print(q.front())
    print(q.dequeue())
    print(q)
    q.equeue(5)
    q.equeue(7)
    print(q)
    q.remove_last_node()
    print(q)
    q.insert_at_index(77, 1)
    print(q)


