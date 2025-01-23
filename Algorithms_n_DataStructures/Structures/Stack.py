from LinkedList import LinkedList


class Stack(LinkedList):
    def __init__(self):
        super().__init__()

    def is_empty(self):
        return self.head is None

    def push(self, data):
        self.insert_at_begin(data)

    def pop(self):
        if self.is_empty():
            raise IndexError('Nothing to pop from empty stack')

        else:
            popped_val = self.head.data
            self.remove_first_node()
            return popped_val

    def peek(self):
        if self.is_empty():
            raise IndexError('Nothing to peek from empty stack')

        else:
            return self.head.data

if __name__ == "__main__":

    s = Stack()
    print(s)
    print(s.is_empty())
    print(len(s))
    s.push(5)
    s.push(6)
    print(s.peek())
    print(s.pop())
    print(s)
    print(len(s))
    s.push(1)
    s.push(100)
    print(s)
    print(s.peek())
    print(len(s))