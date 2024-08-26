n, k = map(int, input().split())
a = list(map(int, input().split()))


class Stack:
    def __init__(self):
        self.curr_vals = []
        self.max_vals = []
        self.min_vals = []

    def push(self, x):
        if self.is_empty():
            self.max_vals.append(x)
            self.min_vals.append(x)
        else:
            self.max_vals.append(max(x, self.max_vals[-1]))
            self.min_vals.append(min(x, self.min_vals[-1]))
        self.curr_vals.append(x)

    def pop_back(self) -> int:
        self.max_vals.pop()
        self.min_vals.pop()
        return self.curr_vals.pop()

    def is_empty(self) -> bool:
        return len(self.curr_vals) == 0

    def min_val(self) -> int:
        return float('inf') if self.is_empty() else self.min_vals[-1]

    def max_val(self) -> int:
        return float('-inf') if self.is_empty() else self.max_vals[-1]


stack1 = Stack()
stack2 = Stack()
count = 0
l = 0

for r in range(n):
    stack2.push(a[r])

    while max(stack2.max_val(), stack1.max_val()) - min(stack2.min_val(), stack1.min_val()) > k and l <= r:
        if stack1.is_empty():
            while not stack2.is_empty():
                stack1.push(stack2.pop_back())
        stack1.pop_back()
        l += 1

    count += r - l + 1

print(count)
