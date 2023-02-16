# https://school.programmers.co.kr/learn/courses/30/lessons/12978
from collections import deque, defaultdict
from heapq import heappop, heappush

"""
최단거리 - 다익스트라 
"""


def solution(N, road, K):
    graph = defaultdict(list)
    for u, v, w in road:
        graph[u].append((v, w))
        graph[v].append((u, w))

    q = [(0, 1)]  # time, node
    dist = defaultdict(int)  # 1에서 i까지 가는 최소비용

    while q:
        time, node = heappop(q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time+w
                heappush(q, (alt, v))

    return int(sum(1 for val in dist.values() if val <= K))


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2],
                   [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
