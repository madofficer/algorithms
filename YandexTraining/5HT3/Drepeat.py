n, k = map(int, input().split())
a = list(map(int, input().split()))

nums = {x: [] for x in a}
def solve():
    for index, num in enumerate(a):
        nums[num].append(index)
    for element in nums.values():
        for i in range(len(element) - 1):
            if element[i] + k >= element[i + 1]:
                return True
    return False

print("YES" if solve() else "NO")
