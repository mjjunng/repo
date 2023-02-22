# https://school.programmers.co.kr/learn/courses/30/lessons/159993
from collections import deque


def solution(maps):
    maps = list(list(maps[i]) for i in range(len(maps)))
    N, M = len(maps), len(maps[0])
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                sr, sc = i, j
            elif maps[i][j] == 'E':
                er, ec = i, j

    dist = [[[-1] * M for _ in range(N)] for _ in range(2)]
    dist[0][sr][sc] = 0
    q = deque([(sr, sc, 0)])
    while q:
        r, c, k = q.popleft()

        for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nr, nc = r+dr, c+dc

            if not(0 <= nr < N) or not(0 <= nc < M) or maps[nr][nc] == 'X' or dist[k][nr][nc] >= 0:
                continue

            if maps[nr][nc] == 'L' and k == 0:
                dist[1][nr][nc] = dist[k][r][c]+1
                q.append((nr, nc, 1))
            elif (nr, nc) == (er, ec) and k:
                return dist[k][r][c]+1
            else:
                dist[k][nr][nc] = dist[k][r][c]+1
                q.append((nr, nc, k))

    return -1
