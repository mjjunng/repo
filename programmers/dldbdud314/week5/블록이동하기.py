"""
BFS 활용 -> 풀이 참고 !
- 현재 위치에서 이동할 수 있는 모든 경우 탐색, 방문 큐에 삽입
i. 평행 이동(상하좌우)
ii. 회전 이동 (가로로 눕혀진 경우 / 세로로 세워진 경우)

중요 자료구조
- 로봇 위치 : {(x1, y1), (x2, y2)} -> 방문 여부 확인 편의성 !
"""
from collections import deque


def is_in_range(n, x, y):
    return 0 <= x < n and 0 <= y < n


def movable(pos1, pos2, board):
    n = len(board)
    next_pos_lst = []
    pos1_x, pos1_y, pos2_x, pos2_y = pos1[0], pos1[1], pos2[0], pos2[1]
    # 평행 이동 -> 두 pos 쌍 모두 해당 방향으로 이동할 수 있는가?
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nxt_pos1_x, nxt_pos1_y, nxt_pos2_x, nxt_pos2_y = pos1_x + dx, pos1_y + dy, pos2_x + dx, pos2_y + dy
        if is_in_range(n, nxt_pos1_x, nxt_pos1_y) and board[nxt_pos1_x][nxt_pos1_y] == 0 and is_in_range(n, nxt_pos2_x,
                                                                                                         nxt_pos2_y) and \
                board[nxt_pos2_x][nxt_pos2_y] == 0:
            next_pos_lst.append({(nxt_pos1_x, nxt_pos1_y), (nxt_pos2_x, nxt_pos2_y)})
    # 회전 이동 : 가로로 눕혀진 경우 / 세로로 세워진 경우
    if pos1_x == pos2_x:  # 가로
        for i in [-1, 1]:  # 위, 아래 -> 모두 0이면 회전 이동 가능
            if is_in_range(n, pos1_x + i, pos1_y) and board[pos1_x + i][pos1_y] == 0 and is_in_range(n, pos2_x + i,
                                                                                                     pos2_y) and \
                    board[pos2_x + i][pos2_y] == 0:
                next_pos_lst.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos_lst.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    elif pos1_y == pos2_y:  # 세로
        for j in [-1, 1]:  # 왼, 오 -> 모두 0이면 회전 이동 가능
            if is_in_range(n, pos1_x, pos1_y + j) and board[pos1_x][pos1_y + j] == 0 and is_in_range(n, pos2_x,
                                                                                                     pos2_y + j) and \
                    board[pos2_x][pos2_y + j] == 0:
                next_pos_lst.append({(pos1_x, pos1_y), (pos1_x, pos1_y + j)})
                next_pos_lst.append({(pos2_x, pos2_y), (pos2_x, pos2_y + j)})
    return next_pos_lst


def solution(board):
    n = len(board)
    queue = deque([({(0, 0), (0, 1)}, 0)])  # pos, time 저장
    visited = [{(0, 0), (0, 1)}]  # 방문한 좌표 쌍 set 저장
    while queue:
        pos, time = queue.popleft()

        if (n - 1, n - 1) in pos:
            return time

        for nxt_pos in movable(*pos, board):
            if nxt_pos not in visited:
                queue.append((nxt_pos, time + 1))
                visited.append(nxt_pos)


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
