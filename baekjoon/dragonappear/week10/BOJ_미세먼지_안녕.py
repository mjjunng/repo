# https://www.acmicpc.net/problem/17144
from sys import stdin
from collections import deque
input = stdin.readline


def spread():
    d = [[0] * C for _ in range(R)]
    rst = [[0] * C for _ in range(R)]
    q = deque()
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                d[i][j] = 0
                q.append((i, j))

    while q:
        r, c = q.popleft()
        cnt = 0
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r+dr, c+dc
            if not(0 <= nr < R) or not(0 <= nc < C) or board[nr][nc] == -1:
                continue
            cnt += 1
            d[nr][nc] += (board[r][c]//5)
        rst[r][c] += (board[r][c]//5)*cnt

    for i in range(R):
        for j in range(C):
            if d[i][j] > 0:
                board[i][j] += d[i][j]
            if rst[i][j] > 0:
                board[i][j] -= rst[i][j]


def clean(sr, sc, dr_dc):
    dir = 0
    r, c = sr, sc
    dr, dc = dr_dc[dir]
    while True:
        nr, nc = r+dr, c+dc
        while not(0 <= nr < R) or not(0 <= nc < C):
            dir = (dir+1) % 4
            dr, dc = dr_dc[dir]
            nr, nc = r+dr, c+dc

        if (nr, nc) == (sr, sc):
            break

        if board[r][c] != -1:
            tmp[nr][nc] = board[r][c]
        else:
            tmp[nr][nc] = 0
        r, c = nr, nc

    for i in range(R):
        for j in range(C):
            board[i][j] = tmp[i][j]


R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

cleaner = []
for i in range(R):
    for j in range(C):
        if board[i][j] == -1:
            cleaner.append((i, j))

(ur, uc), (br, bc) = cleaner
t = 0
while t < T:
    spread()
    tmp = [elem[:] for elem in board]
    clean(ur, uc, [(0, 1), (-1, 0), (0, -1), (1, 0)])
    clean(br, bc, [(0, 1), (1, 0), (0, -1), (-1, 0)])
    t += 1

print(int(sum(board[i][j] for i in range(R)
      for j in range(C) if board[i][j] > 0)))
