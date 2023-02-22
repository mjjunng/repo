"""
** BFS
- 먼저 레버로 이동 -> 출구로 이동하는 최단 시간 구하기 (두번의 BFS)
- 둘 중 하나라도 불가능 하면 -1
"""

from collections import deque


def bfs(maps, sx, sy, tx, ty):  # 시작점, 끝점
    n, m = len(maps), len(maps[0])  # 세로 길이, 가로 길이
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    visited = [[False] * m for _ in range(n)]
    queue = deque([(sx, sy, 0)])
    visited[sx][sy] = True
    while queue:
        cx, cy, time = queue.popleft()
        if cx == tx and cy == ty:
            return time
        for dx, dy in dirs:
            if 0 <= cx + dx < n and 0 <= cy + dy < m and not visited[cx + dx][cy + dy] and maps[cx + dx][
                cy + dy] != 'X':
                visited[cx + dx][cy + dy] = True
                queue.append((cx + dx, cy + dy, time + 1))

    return -1  # 찾지 못한 경우


def solution(maps):
    # 출발점, 레버, 출구 위치 저장
    start, lever, ext = None, None, None
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'E':
                ext = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)

    # 출발 -> 레버 최단 거리 구하기
    t1 = bfs(maps, *start, *lever)

    # 레버 -> 출구 최단 거리 구하기
    t2 = bfs(maps, *lever, *ext)

    if t1 == -1 or t2 == -1:  # 도달 불가
        return -1

    return t1 + t2
