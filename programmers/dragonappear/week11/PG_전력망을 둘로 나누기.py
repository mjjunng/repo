# https://school.programmers.co.kr/learn/courses/30/lessons/86971
from collections import defaultdict


def solution(n, wires):

    def dfs(u):
        nonlocal cnt

        for v in graph[u]:
            if vis[v]:
                continue
            cnt += 1
            vis[v] = True
            dfs(v)

    graph = defaultdict(list)

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    mn = float('inf')
    for a, b in wires:
        vis = [False] * (n+1)

        vis[a] = vis[b] = True
        cnt = 1
        dfs(a)
        r1 = cnt

        cnt = 1
        dfs(b)
        r2 = cnt

        mn = min(mn, abs(r1-r2))

    return mn


"""
DFS
O(N^2)
"""
