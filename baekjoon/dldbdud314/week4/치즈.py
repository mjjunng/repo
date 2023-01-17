"""
시뮬레이션, 구현 (DFS)

- 내부에 있는 공기와 외부에 있는 공기 나눠서 저장 -> airs: 외부 공기는 'O', 내부 공기는 'I'
    - 모두 외부 공기인 경우 -> break
- 치즈에 대해 DFS 탐색 -> 외부에 있는 공기와 두면이 맞닿은 경우 'C' 표시
- 'C' 표시된 부분 제거 (-> 0)
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 상하좌우


def dfs_fill_outer(cx, cy, airs):
    airs[cx][cy] = 'O'  # 외부 공기 표시
    for dx, dy in dirs:
        if 0 <= cx + dx < n and 0 <= cy + dy < m and cheese[cx + dx][cy + dy] == 0 and airs[cx + dx][cy + dy] is None:
            dfs_fill_outer(cx + dx, cy + dy, airs)


def check_outer(airs):
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 0 and airs[i][j] is None:
                dfs_fill_outer(i, j, airs)
                return  # DFS 한번 돌고 끝내야..! (외부 공기 한번)


def check_inner(airs):
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 0 and airs[i][j] is None:  # 공기지만 외부 공기로 표시 안된 경우 -> 내부 공기로 간주
                airs[i][j] = 'I'


def check_air(airs):
    # 처음 DFS 탐색하며 만나는 공기 == 외부 공기
    check_outer(airs)  # 외부 공기 -> 'O'로 표시하기
    check_inner(airs)  # 내부 공기 -> 'I'로 표시하기


def all_airs(airs):  # 전부 공기인지 확인
    total = 0
    for air in airs:
        total += air.count('O')
    return True if total == n * m else False


def meets_air(x, y, airs):
    cnt = 0
    for dx, dy in dirs:
        if 0 <= x + dx < n and 0 <= y + dy < m and airs[x+dx][y+dy] == 'O':
            cnt += 1
    return cnt >= 2


n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]

time = 0
while True:
    airs = [[None] * m for _ in range(n)]  # 내부 공기/외부 공기 확인용 배열
    check_air(airs)  # 내부에 있는 공기와 외부에 있는 공기 체크
    if all_airs(airs):  # 만약 전부 외부 공기('O')인 경우 루프 탈출
        break

    to_melt = []  # 녹일 위치 저장
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1 and meets_air(i, j, airs):  # 외부 공기 2군데 이상 만나는지 확인하고 배열에 저장
                to_melt.append((i, j))  # 녹일 치츠 위치

    # 치즈 녹이기 (1->0)
    for ci, cj in to_melt:
        cheese[ci][cj] = 0  # 공기로 변함 (0)

    time += 1

print(time)
