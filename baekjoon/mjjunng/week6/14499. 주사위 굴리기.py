import sys

def rotate(dir):
    a, b, c, d, e, f = dice
    if dir == 1:  # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif dir == 2:  # 서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif dir == 3:  # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e


if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n, m, y, x, k = map(int, input().split())
    board = []
    dice = [0, 0, 0, 0, 0, 0]   # 위, 뒤, 오, 왼, 앞, 바닥
    dy = [0, 0, 0, -1, 1]
    dx = [0, 1, -1, 0, 0]

    for _ in range(n):
        board.append(list(map(int, input().split())))

    orders = list(map(int, input().split()))
    ny, nx = y, x

    for order in orders:
        ny += dy[order]
        nx += dx[order]

        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            ny -= dy[order]
            nx -= dx[order]
            continue

        # 주사위 이동
        rotate(order)

        # 지도의 칸이 0이면 지도에 주사위 바닥면 숫자 복사
        if board[ny][nx] == 0:
            board[ny][nx] = dice[-1]
        else:   # 0이 아니면 지도의 수가 주사위 바닥에 복사
            dice[-1] = board[ny][nx]
            board[ny][nx] = 0

        print(dice[0])

