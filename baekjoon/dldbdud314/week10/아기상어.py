"""
16236. 아기 상어

**구현 (시뮬레이션)
- 공간 탐색 :
    - 각각의 먹을 수 있는 물고기 별 최단 거리 계산, 해당 물고기 거리별 정렬
- 가장 가까운 물고기 있는 곳으로 이동해서 물고기 먹기
- 크기 만큼 먹었으면 아기 상어 크기++

# 아기 상어의 위치 = 9 -> size >= 9인 경우 무한 루프 주의
# 차라리 아기 상어를 -1 이런 걸로 저장 하던지 / 최단거리 탐색 전에 초기화 하던지
"""
from collections import deque


# BFS : 먹을 수 있는 물고기들과의 최단거리 계산
def find_shortest_path(n, board, sx, sy, size):
    res = []  # 먹을 수 있는 물고기 위치 목록
    visited = [[False] * n for _ in range(n)]
    visited[sx][sy] = True  # 상어 자리
    queue = deque([(sx, sy, 0)])
    min_len = float('inf')
    while queue:
        cx, cy, cl = queue.popleft()

        if 0 < board[cx][cy] < size:
            if cl <= min_len:
                min_len = cl
                res.append((cl, cx, cy))  # 거리, 위치
            continue

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if 0 <= cx + dx < n and 0 <= cy + dy < n and 0 <= board[cx + dx][cy + dy] <= size and not visited[cx + dx][cy + dy]:
                visited[cx + dx][cy + dy] = True
                queue.append((cx + dx, cy + dy, cl + 1))

    return sorted(res, key=lambda x: (-x[0], x[1], x[2]))  # 거리, 위치 순 정렬


def solution(n, board):
    time = 0
    sx, sy = None, None  # 상어 좌표
    for i in range(n):  # 초기 상어 위치
        for j in range(n):
            if board[i][j] == 9:
                sx, sy = i, j
                break
    size = 2
    yumyum = 0  # 먹은 물고기 수
    while True:
        board[sx][sy] = 0  # 기존 위치 (최단거리 탐색 전에 상어 위치 처리 해야 시간 초과 나지 않음)

        # 물고기와의 최단거리 계산
        infos = find_shortest_path(n, board, sx, sy, size)
        if not infos:
            break
        ml, fx, fy = infos[0]

        # 가장 가까운 물고기 먹기
        sx, sy = fx, fy  # 상어 이동
        board[sx][sy] = 9
        yumyum += 1
        time += ml

        if yumyum == size:  # 크기++
            size += 1
            yumyum = 0

    return time


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

print(solution(n, board))
