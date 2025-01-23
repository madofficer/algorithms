from typing import List
from collections import deque


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        edges = [[i + 1] for i in range(n - 1)]
        edges.append([])
        res = [0] * len(queries)

        for i, e in enumerate(queries):
            u, v = e
            edges[u].append(v)

            dist = [0] * n
            q = deque([0])
            while q:
                vertex = q.popleft()
                for j in edges[vertex]:
                    if not dist[j]:
                        dist[j] = dist[vertex] + 1
                        q.append(j)
            res[i] = dist[n - 1]

        return res


print(Solution().shortestDistanceAfterQueries(14, [[1, 7], [6, 9], [6, 13]]))
