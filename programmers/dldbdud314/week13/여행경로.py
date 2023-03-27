"""
** DFS 그래프 순회
- graph[출발지] = [도착지1, 도착지2,..] -> 선 sorting
- backtracking 필요..~
"""
from collections import defaultdict

success = False  # backtracking용 Flag
res = None  # PATH 결과


def all_visited(visited):  # 모든 티켓을 다 썼는가 ?
    for k in visited.keys():
        if not all(visited[k]):
            return False
    return True


def dfs(cur, path, graph, visited, N):
    global success, res
    if len(path) == N + 1 and all_visited(visited):  # 종료 조건 -> path 길이 충족, 모든 티켓 사용
        success = True
        res = path
        return

    for i in range(len(graph[cur])):
        nxt = graph[cur][i]
        if not visited[cur][i]:
            visited[cur][i] = True
            path.append(nxt)
            dfs(nxt, path, graph, visited, N)

            if not success:  # 더 방문할 건 없지만 모든 티켓 활용 못함
                path.pop()
                visited[cur][i] = False


def solution(tickets):
    graph = defaultdict(list)
    visited = defaultdict(list)  # 티켓 단위로 방문 처리
    for a, b in tickets:
        graph[a].append(b)
        visited[a].append(False)

    for k in graph.keys():  # 알파벳 순 정렬 (방문 순서 보장)
        graph[k].sort()

    dfs("ICN", ["ICN"], graph, visited, len(tickets))

    return res


# 놓친 edge case : 동일한 티켓 두개
print(solution(
    [["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"], ["BBB", "AAA"]]))
