"""
** DFS
"""


# 하나의 네트워크 찾기
def dfs(n, i, computers, visited):
    visited[i] = True
    for j in range(n):
        if i != j and not visited[j] and computers[i][j] == 1:
            dfs(n, j, computers, visited)


def solution(n, computers):
    count = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(n, i, computers, visited)
            count += 1

    return count
