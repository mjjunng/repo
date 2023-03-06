# https://www.acmicpc.net/problem/2150
from sys import stdin, setrecursionlimit
from collections import defaultdict
input = stdin.readline
setrecursionlimit(int(1e9))


def dfs(u):
    global id

    id += 1
    p[u] = id
    stack.append(u)  # 스택에 자기 자신을 삽입

    parent = p[u]
    for v in graph[u]:
        if not p[v]:  # 방문하지 않은 이웃
            parent = min(parent, dfs(v))
        elif not finish[v]:  # 처리 중인 이웃
            parent = min(parent, p[v])

    if parent == p[u]:  # scc 완료 처리
        tmp = []
        while True:
            t = stack.pop()
            tmp.append(t)
            finish[t] = True
            if t == u:
                break
        scc.append(tmp)

    return parent


V, E = map(int, input().split())
finish = [False] * (V+1)
p = [0] * (V+1)
scc = []
stack = []
id = 0

graph = defaultdict(list)
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)


for i in range(1, V+1):
    if finish[i]:
        continue
    dfs(i)

for elem in scc:
    elem.sort()
    elem.append(-1)
scc.sort()

print(len(scc))
for elem in scc:
    print(*elem)


"""
타잔 알고리즘
"""
