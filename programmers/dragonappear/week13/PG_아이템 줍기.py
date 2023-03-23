# https://school.programmers.co.kr/learn/courses/30/lessons/87694
from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):

    def draw():
        for rec in rectangle:
            x1, y1, x2, y2 = map(lambda x: x*2, rec)
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    if x1 < i < x2 and y1 < j < y2:
                        board[i][j] = 0
                    elif board[i][j] != 0:
                        board[i][j] = 1

    def bfs():
        dist = [[-1] * MAX for _ in range(MAX)]
        q = deque([(characterX*2, characterY*2)])
        dist[characterX*2][characterY*2] = 1

        while q:
            r, c = q.popleft()

            if (r, c) == (itemX*2, itemY*2):
                return dist[r][c]//2

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r+dr, c+dc

                if dist[nr][nc] == -1 and board[nr][nc] == 1:
                    q.append((nr, nc))
                    dist[nr][nc] = dist[r][c]+1

    MAX = 102
    board = [[-1] * MAX for _ in range(MAX)]
    draw()
    return bfs()


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [
      4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
