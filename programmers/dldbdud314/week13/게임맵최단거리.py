"""
** BFS 최단거리
"""
from collections import deque


def solution(maps):
    N, M = len(maps), len(maps[0])

    queue = deque([(0, 0, 1)])  # (x, y, l)
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    while queue:
        cx, cy, l = queue.popleft()

        if (cx, cy) == (N - 1, M - 1):
            return l

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if 0 <= cx + dx < N and 0 <= cy + dy < M and maps[cx + dx][cy + dy] == 1 and not visited[cx + dx][cy + dy]:
                visited[cx + dx][cy + dy] = True
                queue.append((cx + dx, cy + dy, l + 1))

    return -1
