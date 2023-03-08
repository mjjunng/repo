"""
** 백트래킹, DFS
- 현재 최소 피로도 조건 충족 시 dfs 탐색 수행
"""
max_visit = 0


def dfs(visited, cur_k, dungeons):
    global max_visit
    cur_cnt = visited.count(True)
    if cur_cnt > max_visit:
        max_visit = cur_cnt

    for i in range(len(dungeons)):
        if not visited[i] and cur_k >= dungeons[i][0]:
            visited[i] = True
            dfs(visited, cur_k - dungeons[i][1], dungeons)
            visited[i] = False


def solution(k, dungeons):
    dfs([False] * len(dungeons), k, dungeons)
    return max_visit


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
