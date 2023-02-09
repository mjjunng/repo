import sys
from collections import deque


'''
    bfs: 실패 
     
'''

# 벽이 아래로 내려가는 로직
def down(board):
    res = [['.' for _ in range(8)] for _ in range(8)]

    for i in range(1, 8):
        for j in range(8):
            res[i][j] = board[i-1][j]

    return res

if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    board = []
    q = deque()
    dy = [0, 1, -1, 0, 0, -1, -1, 1, 1]
    dx = [0, 0, 0, 1, -1, -1, 1, -1, 1]
    answer = 0
    visited = [[0 for _ in range(8)] for _ in range(8)]

    for _ in range(8):
        board.append(list(input()))

    visited[7][0] = 1
    q.append([7, 0, board, visited])

    while q:
        y, x, b, v = q.popleft()

        # 이동한 위치가 벽인 경우 이동 불가능
        if b[y][x] == '#':
            continue

        if y == 0 and x == 7:
            answer = 1
            break

        # 캐릭터 이동
        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]

            if (0 <= ny < 8) and (0 <= nx < 8):
                if b[ny][nx] == '.' and v[ny][nx] == 0:
                    v[ny][nx] = 1
                    q.append([ny, nx, down(b), v])


    print(answer)
