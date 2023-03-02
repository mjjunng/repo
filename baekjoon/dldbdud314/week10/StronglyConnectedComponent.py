"""
2150. Strongly Connected Component

** 강한 연결 요소 알고리즘 (DFS & stack 활용) - 풀참.. 어렵,,
"""
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(x):
    global _id
    _id += 1
    d[x] = _id
    stack.append(x)

    parent = d[x]
    for y in graph[x]:
        if d[y] == 0:  # 아직 방문하지 않은 경우
            parent = min(parent, dfs(y))
        elif not finished[y]:  # 방문 했지만 scc 처리 중
            parent = min(parent, d[y])

    if parent == d[x]:  # 자기 자신이 부모 노드인 경우 - scc 완료, stack 비우기
        cur_scc = []
        while stack:
            node = stack.pop()
            cur_scc.append(node)
            finished[node] = True
            if node == x:
                break
        scc.append(sorted(cur_scc))

    return parent


v, e = map(int, input().split())
# parent : [child1, child2, ...]
# parent -> child 방향
graph = defaultdict(list)
for _ in range(e):
    p, c = map(int, input().split())
    graph[p].append(c)

_id = 0
d = [0] * (v + 1)  # 노드별 고유 id
stack = []
finished = [False] * (v + 1)  # 해당 노드 scc 처리 완료 여부

scc = []
for i in range(1, v + 1):
    if not finished[i]:
        dfs(i)

scc.sort()

print(len(scc))
for x in scc:
    print(*x, end=' ')
    print(-1)
