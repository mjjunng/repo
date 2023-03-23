# https://school.programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque


def solution(maps):
    def bfs():
        dist = [[-1] * M for _ in range(N)]
        q = deque([(0, 0)])
        dist[0][0] = 1

        while q:
            r, c = q.popleft()

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r+dr, c+dc

                if not(0 <= nr < N) or not(0 <= nc < M) or maps[nr][nc] == 0 or dist[nr][nc] > -1:
                    continue

                if (nr, nc) == (N-1, M-1):
                    return dist[r][c]+1

                dist[nr][nc] = dist[r][c]+1
                q.append((nr, nc))

        return -1

    N, M = len(maps), len(maps[0])

    return bfs()


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
      1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))

print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
      1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
