"""
DP + BFS - 풀이 참고
"""
from collections import deque
INF = int(1e9)


def bfs(board, start):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    n = len(board)
    visited = [[INF] * n for _ in range(n)]
    visited[0][0] = 0

    queue = deque([start])  # x, y, cost, dir
    while queue:
        cx, cy, cc, cd = queue.popleft()

        for i in range(4):
            nx = cx + dirs[i][0]
            ny = cy + dirs[i][1]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                # 진행 방향에 따른 비용 추가
                nc = cc + 100 if i == cd else cc + 600
                if nc < visited[nx][ny]:  # 기존 비용 보다 작은 경우 탐색 계속
                    visited[nx][ny] = nc
                    queue.append([nx, ny, nc, i])

    return visited[-1][-1]


def solution(board):
    return min([bfs(board, (0, 0, 0, 0)), bfs(board, (0, 0, 0, 1))])
