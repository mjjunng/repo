# https://www.acmicpc.net/problem/16929
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(int(1e9))


"""
dfs로 사이클 판별
"""


def dfs(r, c, pr, pc, color):
    for dr, dc in dr_dc:
        nr, nc = r+dr, c+dc
        if not(0 <= nr < N) or not(0 <= nc < M) or board[nr][nc] != color or (nr, nc) == (pr, pc):
            continue

        if vis[nr][nc]:
            return True

        vis[nr][nc] = True
        rst = dfs(nr, nc, r, c, color)
        if rst:
            return rst
    return False


N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
dr_dc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
vis = [[False]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if vis[i][j]:
            continue
        vis[i][j] = True
        rst = dfs(i, j, -1, -1, board[i][j])
        if rst:
            print("Yes")
            exit()

print("No")
