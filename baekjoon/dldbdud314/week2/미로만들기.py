'''
BRUTEFORCE (시뮬레이션 유형): O(n)

(50, 50)을 출발점으로, 명령어 따라 이동한다 (이동하면서 '.' 표시)
왼쪽-위(최소x, 최소y)와 오른쪽-아래(최대x, 최대y)를 구해서,
그 외의 지점을 벽('#')으로 채우며 결과 출력
'''

dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # 아래, 왼, 위, 오른


def turn_right(idx):  # 오른쪽으로 방향 전환
    if idx + 1 >= 4:
        idx = 0
    else:
        idx += 1
    return idx


def turn_left(idx):  # 왼쪽으로 방향 전환
    if idx - 1 < 0:
        idx = 3
    else:
        idx -= 1
    return idx


n = int(input())
moves = input()

# 미로 이동하며 표시
area = [['-'] * 101 for _ in range(101)]

x, y = 50, 50
area[x][y] = '.'  # 시작점
positions = [(x, y)]  # 이동 위치 기록
idx = 0
dx, dy = dirs[idx]  # 이동할 방향 : default 남쪽
for move in moves:
    if move == 'R':
        idx = turn_right(idx)
        dx, dy = dirs[idx]
    elif move == 'L':
        idx = turn_left(idx)
        dx, dy = dirs[idx]
    elif move == 'F':
        x += dx
        y += dy
        area[x][y] = '.'
        positions.append((x, y))

# 왼쪽 시작점, 오른쪽 끝점 구분하기
min_x, min_y = float('inf'), float('inf')
max_x, max_y = -float('inf'), -float('inf')
for xx, yy in positions:
    min_x, min_y = min(min_x, xx), min(min_y, yy)
    max_x, max_y = max(max_x, xx), max(max_y, yy)

# 결과 출력
for i in range(min_x, max_x + 1):
    for j in range(min_y, max_y + 1):
        if area[i][j] != '.':
            print('#', end = '')
        else:
            print(area[i][j], end = '')
    print()