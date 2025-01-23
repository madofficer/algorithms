import ctypes


class Array:
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.Array = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, index):

        if not (0 <= index < self.n):
            raise IndexError("Index is out of bounds")

        return self.Array[index]

    def __str__(self):
        return "[" + ", ".join(str(self.Array[i]) for i in range(self.n)) + "]"

    def _is_empty(self) -> bool:
        return self.n == 0

    def append(self, element):

        if self.n == self.capacity:
            self._resize(2 * self.capacity)

        self.Array[self.n] = element
        self.n += 1

    def insert_at(self, item, index):

        if not (0 <= index < self.n):
            raise IndexError("Index is out of bounds")

        if self.n == self.capacity:
            self._resize(2 * self.capacity)

        for i in range(self.n - 1, index - 1, -1):
            self.Array[i + 1] = self.Array[i]

        self.Array[index] = item
        self.n += 1

    def delete(self):

        if self._is_empty():
            raise IndexError("Array is empty, impossible to delete")

        self.Array[self.n - 1] = 0
        self.n -= 1

    def remove_at(self, index):

        if self._is_empty():
            raise IndexError("Array is empty, impossible to delete")

        if not (0 <= index < self.n):
            raise IndexError("Index is out of bounds")

        if index == self.n - 1:
            self.Array[self.n - 1] = 0
            self.n -= 1
            return

        for i in range(index, self.n - 1):
            self.Array[i] = self.Array[i + 1]

        self.Array[self.n - 1] = 0
        self.n -= 1

    def _resize(self, new_capacity):
        B = self.make_array(new_capacity)
        for i in range(self.n):
            B[i] = self.Array[i]

        self.Array = B
        self.capacity = new_capacity

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()


arr = Array()
arr.append(1)
arr.append(7)
print(arr)
print(len(arr))
arr.delete()
arr.append(1)
arr.append(124)
arr.append(100)
print(arr)
arr.remove_at(2)
arr.insert_at(777, 2)
print(arr)