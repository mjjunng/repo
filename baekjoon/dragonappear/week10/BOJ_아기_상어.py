# https://www.acmicpc.net/problem/16236
from sys import stdin
from collections import deque
from heapq import heappush, heappop
input = stdin.readline


def bfs(sr, sc, size):
    dist[sr][sc] = 0
    q = deque([(sr, sc)])

    while q:
        r, c = q.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r+dr, c+dc

            if not(0 <= nr < N) or not(0 <= nc < N) or board[nr][nc] > size or dist[nr][nc] > -1:
                continue

            dist[nr][nc] = dist[r][c]+1
            q.append((nr, nc))


N = int(input())
board = [list(map(int, input().strip().split())) for _ in range(N)]

fish = 0
sr = sc = -1
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            sr, sc = i, j
        elif board[i][j]:
            fish += 1

size = 2
ans = 0
cnt = 0
while fish:
    dist = [[-1] * N for _ in range(N)]
    bfs(sr, sc, size)

    heap = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 or board[i][j] >= size or dist[i][j] == -1:
                continue
            heappush(heap, (dist[i][j], i, j))

    if not heap:
        break

    d, x, y = heappop(heap)

    # 물고기 먹기
    board[x][y], board[sr][sc] = 0, 0
    fish -= 1
    cnt += 1

    ans += d
    sr, sc = x, y

    if size == cnt:
        size += 1
        cnt = 0

print(ans)
