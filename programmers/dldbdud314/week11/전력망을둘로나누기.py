"""
** 완전 탐색, 그래프 DFS
- 각각의 연결 관계 끊어 보고
- 두 개의 노드를 시작으로 dfs 돌면서
- 각각 몇개의 노드가 있는지 개수 세고 최소 차이 갱신
"""
from copy import deepcopy


def dfs(cur, graph, visited):
    for nxt in graph[cur]:
        if nxt not in visited:
            visited.add(nxt)
            dfs(nxt, graph, visited)

    return len(visited)


def cut(p1, p2, graph, n):
    # 연결을 끊고
    graph[p1].remove(p2)
    graph[p2].remove(p1)

    # 각 노드를 시작점으로 dfs
    cnt1 = dfs(p1, graph, {p1})  # p1 시작으로 dfs 탐색
    cnt2 = dfs(p2, graph, {p2})  # p2 시작으로 dfs 탐색

    return abs(cnt1 - cnt2)


def solution(n, wires):
    # 양방향 연결 그래프 만들기
    graph = {w: [] for w in range(1, n + 1)}
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    min_diff = float('inf')
    for a, b in wires:  # 모든 연결 관계 끊어보며 최솟값 갱신
        min_diff = min(cut(a, b, deepcopy(graph), n), min_diff)  # dfs 탐색 시작점 두개

    return min_diff


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
