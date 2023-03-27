"""
** 구현 && BFS 최단거리 구하기
- 좌표값 * 2 처리 없이 한참 헤맴.. ㄸㄹㄹ.. ((=> 풀이 참고))
"""
from collections import deque
LEN = 102


def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * LEN for _ in range(LEN)]

    # 공간 색칠
    for x1, y1, x2, y2 in rectangle:
        for i in range(2 * x1, 2 * x2 + 1):
            for j in range(2 * y1, 2 * y2 + 1):
                if board[i][j] == 0:
                    board[i][j] = 1
    # 내부는 0으로
    for x1, y1, x2, y2 in rectangle:
        for i in range(2 * x1 + 1, 2 * x2):
            for j in range(2 * y1 + 1, 2 * y2):
                board[i][j] = 0

    # BFS
    startX, startY = characterX * 2, characterY * 2
    queue = deque([(startX, startY, 0)])
    visited = [[False] * LEN for _ in range(LEN)]
    visited[startX][startY] = True
    while queue:
        cx, cy, cl = queue.popleft()
        if (cx, cy) == (itemX * 2, itemY * 2):
            return cl // 2

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if 0 <= dx + cx < LEN and 0 <= dy + cy < LEN and board[dx + cx][dy + cy] == 1 and not visited[dx + cx][dy + cy]:
                visited[dx + cx][dy + cy] = True
                queue.append((dx + cx, dy + cy, cl + 1))
