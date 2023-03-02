"""
17144. 미세 먼지 안녕!

** 구현 (시뮬레이션)
- t초간:
1. 미세 먼지 확산
    - 미세 먼지 있는 칸 저장
    - 해당 칸들에 대해 확산 후 계산 (새로운 board 사용)
2. 공기청정기 작동
    - 반시계 방향, 시계 방향으로 한칸씩 밀기
"""
r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]


def find_dusts():  # 미먼 위치 기록
    dres = []
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                dres.append((i, j))
    return dres


def spread(dinfo):  # 확산
    new_board = [[0] * c for _ in range(r)]
    new_board[px1][py1], new_board[px2][py2] = -1, -1
    for cx, cy in dinfo:
        to_spread = board[cx][cy] // 5
        spreads = 0
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if 0 <= cx + dx < r and 0 <= cy + dy < c and board[cx + dx][cy + dy] > -1:
                new_board[cx + dx][cy + dy] += to_spread
                spreads += 1
        new_board[cx][cy] += board[cx][cy] - to_spread * spreads

    return new_board


def upper_circulate(px):  # 위쪽 반시계 방향 순환
    for pi in range(px, 0, -1):
        if board[pi][0] == -1:
            continue
        board[pi][0] = board[pi - 1][0]
    for pj in range(1, c):
        board[0][pj - 1] = board[0][pj]
    for pi in range(1, px + 1):
        board[pi - 1][-1] = board[pi][-1]
    for pj in range(c - 1, 0, -1):
        if board[px][pj - 1] == -1:
            board[px][pj] = 0
            continue
        board[px][pj] = board[px][pj - 1]


def lower_circulate(px):  # 아래쪽 시계 방향 순환
    for pi in range(px + 1, r):
        if board[pi - 1][0] == -1:
            continue
        board[pi - 1][0] = board[pi][0]
    for pj in range(1, c):
        board[r - 1][pj - 1] = board[r - 1][pj]
    for pi in range(r - 1, px, -1):
        board[pi][-1] = board[pi - 1][-1]
    for pj in range(c - 1, 0, -1):
        if board[px][pj - 1] == -1:
            board[px][pj] = 0
            continue
        board[px][pj] = board[px][pj - 1]


# 공기청정기 위치
px1, py1, px2, py2 = None, None, None, None
for i in range(r - 1):
    if board[i][0] == -1 and board[i + 1][0] == -1:
        px1, py1 = i, 0
        px2, py2 = i + 1, 0
        break

for _ in range(t):
    dusts = find_dusts()  # 동시에 모든 위치에서 확산 하므로 초기 위치와 먼지 양 기록 필요
    # 미세 먼지 확산
    board = spread(dusts)

    # 공기청정기 작동
    upper_circulate(px1)
    lower_circulate(px2)

total = 2  # 공기청정기 값(-1, -1) 고려
for x in board:
    total += sum(x)

print(total)
