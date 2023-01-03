from copy import deepcopy

# 사각 지대 카운트
def count_area(board):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                cnt += 1
    return cnt

# 감시 영역 체크
def check(board, y, x, dy, dx):
    while True:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < n and 0 <= nx < m:
            if board[ny][nx] == 6:
                break
            elif board[ny][nx] == 0:
                board[ny][nx] = '#'

        else:
            break
        y = ny
        x = nx

def dfs(lev, board):
    global res
    if lev == len(data):
        cnt = count_area(board)
        if cnt < res:
            res = cnt
        return

    kind = data[lev][2]
    y = data[lev][0]
    x = data[lev][1]
    copy_board = deepcopy(board)
    for i in cctv_dir[kind]:
        for j in i:
            check(copy_board, y, x, dir[j][0], dir[j][1])
        dfs(lev+1, copy_board)  # 가지치기 
        copy_board = deepcopy(board)    # back


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = []
    data = []
    res = float('inf')
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    cctv_dir = [
            [],
            [[0], [1], [2], [3]],
            [[0, 1], [2, 3]],
            [[0, 2], [0, 3], [1, 2], [1, 3]],
            [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
            [[0, 1, 2, 3]]
            ]
    for _ in range(n):
        board.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(m):
            if 0 < board[i][j] < 6:
                data.append([i, j, board[i][j]])

    dfs(0, board)
    print(res)

