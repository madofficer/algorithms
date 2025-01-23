from typing import List


class ZigzagIterator:

    def __init__(self, a: List[int], b: List[int]):
        self.a = a
        self.b = b
        self.a_i = 0
        self.b_j = 0
        self.flag = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.a_i < len(self.a) and self.b_j < len(self.b):
            if self.flag:
                self.b_j += 1
                self.flag = 0
                return self.b[self.b_j - 1]
            else:
                self.a_i += 1
                self.flag = 1
                return self.a[self.a_i - 1]
        elif self.a_i == len(self.a) and self.b_j < len(self.b):
            self.b_j += 1
            return self.b[self.b_j - 1]
        elif self.b_j == len(self.b) and self.a_i < len(self.a):
            self.a_i += 1
            return self.a[self.a_i - 1]
        else:
            raise StopIteration


if __name__ == "__main__":
    obj = ZigzagIterator([1], [])
    ans = []
    while True:
        try:
            ans.append(obj.__next__())
        except StopIteration:
            break
    print(ans)

