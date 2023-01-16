"""
DFS -> 현재 노드, 양의 수, 늑대의 수, 방문 가능한 정점 후보들
- 종료 조건: 더 이상 방문할 수 없음 (늑대 == 양)

27.8 / 100.0 -> TO FIX..
"""
from collections import defaultdict
max_lamb_cnt = 0


def dfs(info, graph, node, lamb_cnt, wolf_cnt, possible):
    # print(node, lamb_cnt, wolf_cnt)
    if lamb_cnt <= wolf_cnt:
        return

    global max_lamb_cnt
    max_lamb_cnt = max(max_lamb_cnt, lamb_cnt)

    possible.remove(node)  # 현재 노드 제거
    possible.extend(graph[node])  # 자식 노드들 업뎃
    for nxt in possible:
        dfs(info, graph, nxt, lamb_cnt + int(info[nxt] == 0), wolf_cnt + int(info[nxt] == 1), possible)


def solution(info, edges):
    graph = defaultdict(list)  # 노드별 자식 노드 정보 저장 -> graph[P] = [C1, C2, ...]
    for p, c in edges:
        graph[p].append(c)

    possible = [0]
    dfs(info, graph, 0, 1, 0, possible)

    return max_lamb_cnt


#print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
#               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
               [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))
