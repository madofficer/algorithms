from collections import defaultdict, deque


def is_intersected(event, map1, map2):
    return map1.get(event, 0) > 0 and map2.get(event, 0) > 0


def event_collector(event, map):
    if event in map:
        map[event] -= 1
        if map[event] == 0:
            del map[event]


n = int(input())
events = []

for _ in range(3):
    events.append(list(map(int, input().split())))

map_a = defaultdict(int)
map_b = defaultdict(int)
map_c = defaultdict(int)

for i in range(n):
    map_a[events[0][i]] += 1
    map_b[events[1][i]] += 1
    map_c[events[2][i]] += 1

removed = [False] * n
queue = deque()

for i in range(n):
    if (
            not is_intersected(events[0][i], map_b, map_c)
            or not is_intersected(events[1][i], map_a, map_c)
            or not is_intersected(events[2][i], map_a, map_b)
    ):
        queue.append(i)
        removed[i] = True

while queue:
    index = queue.popleft()

    event_collector(events[0][index], map_a)
    event_collector(events[1][index], map_b)
    event_collector(events[2][index], map_c)

    for i in range(n):
        if not removed[i] and \
                (not is_intersected(events[0][i], map_b, map_c) or
                 not is_intersected(events[1][i], map_a, map_c) or
                 not is_intersected(events[2][i], map_a, map_b)):
            queue.append(i)
            removed[i] = True

print(sum(removed))
