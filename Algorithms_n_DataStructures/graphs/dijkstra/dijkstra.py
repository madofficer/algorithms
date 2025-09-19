import heapq as hq

n, s, f = map(int, input().split())


def dijkstra(start: int, dist: [], edges: [[]]) -> None:
    dist[start] = 0
    heap = []
    hq.heappush(heap, [dist[start], start])  # first elem of heap [distance to current edge, index of current edge]

    while heap:
        # pick the closest vertex from current
        closest = hq.heappop(heap)
        curr_dist, vertex = closest

        # skip iteration if distance to the vertex cant be optimized
        if dist[vertex] < curr_dist:
            continue

        # look throw all edges from current vertex
        for i in range(len(edges[vertex])):
            to, weight = edges[vertex][i]  # unpack destination and its edge weight

            # if shorter way found, push distance and vertex index to heap
            if dist[to] > dist[vertex] + weight:
                dist[to] = dist[vertex] + weight
                hq.heappush(heap, [dist[to], to])


edges = [[] for i in range(n + 1)]  # indexes of edges from 1 to n + 1
dist = [float("inf")] * (n + 1)

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if a[j] != -1:
            edges[i + 1].append([j + 1, a[j]])  # add index and weight from current edge to the next one

dijkstra(s, dist, edges)
print(dist[f] if dist[f] < float("inf") else -1)
