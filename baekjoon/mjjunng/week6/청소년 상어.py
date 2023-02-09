import sys

# 실패 코드 

# 번호가 작은 물고기부터 순서대로 이동
def move_fish(board):

    for k in range(1, 17):
        i = fishes[k][0]
        j = fishes[k][1]
        dir = fishes[k][2] - 1

        # 다음 칸으로 이동 가능한 경우
        ny = i + dy[dir]
        nx = j + dx[dir]
        if (0 <= ny < 4) and (0 <= nx < 4) and board[ny][nx][0] > 0:
            board[i][j], board[ny][nx] = board[ny][nx], board[i][j]
        else:
            # 다음 칸으로 이동 불가능한 경우 -> 45 회전
            while True:
                dir = (dir + 1) % 8
                ry = i + dx[dir]
                rx = j + dx[dir]

                if ry == i and rx == j:
                    break

                if (0 <= ry < 4) and (0 <= rx < 4):
                    board[ry][rx][1] = dir
                    board[i][j], board[ry][rx] = board[ry][rx], board[i][j]
                    break

    return board


def dfs(y, x, ans, board):
    global res
    if ans > res:
        res = ans

    # 상어 이동
    dir = board[y][x][1] - 1
    ny = y + dy[dir]
    nx = x + dx[dir]

    while (0 <= ny < 4) and (0 <= nx < 4):
        fish = board[ny][nx][0]
        board[y][x] = [-1, -1]
        dfs(ny, nx, ans+fish, move_fish(board))

        ny += dy[dir]
        nx += dx[dir]




if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    board = [[] for _ in range(4)]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    res = 0
    fishes = [[] for _ in range(17)]

    for k in range(4):
        data = list(map(int, input().split()))
        j = 0

        # 물고기 번호대로 위치, 방향 저장
        for i in range(0, len(data), 2):
            board[k].append(data[i:i+2])
            fishes[data[i]] = [k, i-j, data[i+1]]
            j += 1


    dfs(0, 0, board[0][0][0], board)

    print(res)



