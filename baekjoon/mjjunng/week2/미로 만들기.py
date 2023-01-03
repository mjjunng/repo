n = int(input())
data = list(input())
board = [[0 for _ in range(101)] for _ in range(101)]
y, x = 50, 50
dy = [1, 0, -1, 0]  # 아, 왼, 위, 오
dx = [0, -1, 0, 1]
cur_dir = 0   # 현재 방향 (남쪽)
board[y][x] = '.'
start_y, start_x = y, x
end_y, end_x = y, x

for i in data:
    if i == 'R':
        cur_dir = (cur_dir + 1) % 4
    elif i == 'L':
        cur_dir = (cur_dir - 1) % 4
    else:
        board[y+dy[cur_dir]][x+dx[cur_dir]] = '.'
        y = y+dy[cur_dir]   # 현재 위치 갱신
        x = x+dx[cur_dir]
        start_y = min(start_y, y)
        start_x = min(start_x, x)
        end_y = max(end_y, y)
        end_x = max(end_x, x)

for i in range(start_y, end_y+1):
    for j in range(start_x, end_x+1):
        if board[i][j] == 0:
            print('#', end='')
        else:
            print(board[i][j], end='')
    print()
