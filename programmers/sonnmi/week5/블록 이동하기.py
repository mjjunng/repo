from collections import deque


def can_move(cur1, cur2, new_board):
    x, y = 0, 1
    cand = []
    # 평행이동
    dic = {0: [-1, 0], 1: [1, 0], 2: [0, 1], 3: [0, -1]}
    for i in range(4):
        nx1 = (cur1[x] + dic[i][0], cur1[y] + dic[i][1])
        nx2 = (cur2[x] + dic[i][0], cur2[y] + dic[i][1])
        if new_board[nx1[x]][nx1[y]] == 0 and new_board[nx2[x]][nx2[y]] == 0:
            cand.append((nx1, nx2))
    # 회전
    if cur1[x] == cur2[x]:  # 가로방향 일 때
        UP, DOWN = -1, 1
        for d in [UP, DOWN]:
            if new_board[cur1[x] + d][cur1[y]] == 0 and new_board[cur2[x] + d][cur2[y]] == 0:
                cand.append((cur1, (cur1[x] + d, cur1[y])))
                cand.append((cur2, (cur2[x] + d, cur2[y])))
    else:  # 세로 방향 일 때
        LEFT, RIGHT = -1, 1
        for d in [LEFT, RIGHT]:
            if new_board[cur1[x]][cur1[y] + d] == 0 and new_board[cur2[x]][cur2[y] + d] == 0:
                cand.append(((cur1[x], cur1[y] + d), cur1))
                cand.append(((cur2[x], cur2[y] + d), cur2))
    return cand


def solution(board):
    # board 외벽 둘러싸기
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    for i in new_board:
        print(i)
    q = deque([((1, 1), (1, 2), 0)])  # 첫번쨰좌표 두번째좌표 시간
    check = set([((1, 1), (1, 2))])  # 방문확인용
    while q:
        cur1, cur2, time = q.popleft()
        if cur1 == (n, n) or cur2 == (n, n):
            return time
        for nxt in can_move(cur1, cur2, new_board):
            if nxt not in check:
                q.append((nxt[0], nxt[1], time + 1))
                check.add(nxt)