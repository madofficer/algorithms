class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        output = ""
        current_node = self.head
        if current_node is None:
            return "[]"
        while current_node.next is not None:
            output += f"{current_node.data}, "
            current_node = current_node.next
        output += f"{current_node.data}"
        return "[" + output + "]"

    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_index(self, data, index):
        if index == 0:
            self.insert_at_begin(data)
            return

        position = 0
        current_node = self.head
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            raise IndexError("Position out of bounds")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node

    def update_node(self, data, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = data

        else:
            while current_node is not None and position != index:
                current_node = current_node.next
                position += 1

            if current_node is not None:
                current_node.data = data
            else:
                raise IndexError("Index out of bounds")

    def remove_first_node(self):
        if self.head is None:
            raise IndexError("Nothing to remove")

        self.head = self.head.next

    def remove_last_node(self):
        if self.head is None:
            raise IndexError("Nothing to remove")

        current_node = self.head
        if current_node.next is None:
            self.remove_first_node()
            return

        while current_node.next.next is not None:
            current_node = current_node.next

        current_node.next = None

    def remove_at_index(self, index):
        if self.head is None:
            raise IndexError("Nothing to remove")

        if index == 0:
            self.remove_first_node()
            return

        current_node = self.head
        position = 0
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node.next is not None:
            current_node.next = current_node.next.next
        elif position == index:
            self.insert_at_end()
        else:
            raise IndexError("Index out of bounds")

    def remove_node(self, data):
        current_node = self.head
        if current_node is None:
            raise IndexError("Nothing to remove")

        if current_node.next is None:
            self.remove_first_node()

        while current_node is not None and current_node.next.data != data:
            current_node = current_node.next

        if current_node is not None:
            current_node.next = current_node.next.next
        else:
            raise ValueError("Value not found in the Linked List")

    def __len__(self):
        n = 0
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next
            n += 1
        return n



if __name__ == "__main__":

    LL = LinkedList()
    print(LL)
    LL.insert_at_begin(1)
    LL.insert_at_begin(2)
    print(LL)
    LL.insert_at_end(5)
    print(LL)
    LL.update_node(4, 2)
    print(LL)
    LL.insert_at_begin(77)
    print(LL)
    LL.update_node(99, 0)
    print(LL)
    LL.insert_at_end(50)
    print(LL)
    LL.remove_first_node()
    LL.remove_last_node()
    print(LL)
    LL.remove_at_index(1)
    LL.remove_at_index(0)
    print(LL)
    LL.insert_at_index(100, 1)
    LL.insert_at_index(123, 0)
    print(LL)
    LL.remove_last_node()
    print(LL)

    LL.remove_last_node()
    print(LL)
    LL.remove_last_node()

    print(LL)
