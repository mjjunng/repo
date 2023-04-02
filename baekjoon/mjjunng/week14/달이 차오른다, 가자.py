import sys
from collections import deque
'''
    a: 000001
    b: 000010
    a, b: 000011
'''

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n, m = map(int, input().split())
    answer = 0
    board = []
    visited = [[[0 for _ in range(64)] for _ in range(m)] for _ in range(n)]

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    q = deque()

    for _ in range(n):
        board.append(list(input()))

    sy, sx = 0, 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == '0':
                sy = i
                sx = j
                q.append([i, j, 0, 0])
                visited[i][j][0] = 1
                board[i][j] = '.'
        if q:
            break
    def bfs():
        while q:
            y, x, cnt, idx = q.popleft()

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if (0 <= ny < n) and (0 <= nx < m) and board[ny][nx] != '#' and visited[ny][nx][idx] == 0:
                    if board[ny][nx] == '.':
                        visited[ny][nx][idx] = 1
                        q.append([ny, nx, cnt+1, idx])

                    elif board[ny][nx] == '1':
                        return cnt+1

                    elif board[ny][nx].isupper():   # 문
                        if idx & 1 << (ord(board[ny][nx])-65):  # 열쇠 있는지 확인
                            visited[ny][nx][idx] = 1
                            q.append([ny, nx, cnt+1, idx])

                    else:   # 키 획득
                        n_idx = idx | (1 << ord(board[ny][nx])-97)
                        if visited[ny][nx][n_idx] == 0:
                            visited[ny][nx][n_idx] = 1
                            q.append([ny, nx, cnt+1, n_idx])

        return -1

    print(bfs())
