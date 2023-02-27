# implementation

import copy
import sys

# 미세먼지 확산
def diffusion(board):
    r = len(board)
    c = len(board[0])
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    new_board = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                cnt = 0     # 확산된 방향의 개수
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]

                    if (0 <= ny < r) and (0 <= nx < c) and board[ny][nx] >= 0:
                        cnt += 1
                        new_board[ny][nx] += board[i][j] // 5

                new_board[i][j] += board[i][j] - (board[i][j] // 5) * cnt

            elif board[i][j] == -1:
                new_board[i][j] = -1

    return new_board

# 순환
def rotation(board, upper, lower):
    r = len(board)
    c = len(board[0])
    new_board = copy.deepcopy(board)
    new_board[upper][0] = -1
    new_board[lower][0] = -1

    # 위쪽
    # →
    new_board[upper][1] = 0
    for i in range(2, c):
        new_board[upper][i] = board[upper][i-1]

    if upper != 0:
        # ↑
        for i in range(upper-1, -1, -1):
            new_board[i][-1] = board[i+1][-1]

        # ←
        for i in range(c-1):
            new_board[0][i] = board[0][i+1]

        # ↓
        for i in range(1, upper):
            new_board[i][0] = board[i-1][0]

    # 아래쪽
    # →
    new_board[lower][1] = 0

    for i in range(2, c):
        new_board[lower][i] = board[lower][i - 1]

    if lower != r-1:
        # ↓
        for i in range(lower + 1, r):
            new_board[i][-1] = board[i - 1][-1]

        # ←
        for i in range(c-2, -1, -1):
            new_board[r-1][i] = board[r-1][i+1]

        # ↑
        for i in range(r-2, lower, -1):
            new_board[i][0] = board[i+1][0]


    return new_board



if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    r, c, t = map(int, input().split())
    board = []
    answer = 0
    upper, lower = 0, 0

    for _ in range(r):
        board.append(list(map(int, input().split())))


    for i in range(r):
        if board[i][0] == -1:
            upper = i
            lower = i + 1
            break

    for _ in range(t):
        board = diffusion(board)
        board = rotation(board, upper, lower)

    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                answer += board[i][j]

    print(answer)
