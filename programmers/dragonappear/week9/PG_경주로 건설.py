# https://school.programmers.co.kr/learn/courses/30/lessons/67259
from collections import deque
INF = float('inf')


def solution(board):

    ans = INF
    N = len(board)
    dr_dc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    dist = [[[INF] * N for _ in range(N)] for _ in range(4)]
    dist[0][0][0] = dist[2][0][0] = 0
    q = deque([(0, 0, 0), (2, 0, 0)])

    while q:
        cur, r, c = q.popleft()

        if r == N-1 and c == N-1:
            ans = min(ans, dist[cur][r][c])
            continue

        for nxt, v in enumerate(dr_dc):
            nr, nc = r+v[0], c+v[1]

            if not(0 <= nr < N) or not(0 <= nc < N) or board[nr][nc] == 1:
                continue

            fee = 100 if nxt == cur else 600

            if dist[nxt][nr][nc] > dist[cur][r][c] + fee:
                dist[nxt][nr][nc] = dist[cur][r][c] + fee
                q.append((nxt, nr, nc))

    return ans
