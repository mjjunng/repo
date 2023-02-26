# bfs 

import sys
from collections import deque

def bfs(y, x, size, n):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    fish = []   # 먹을 수 있는 물고기의 위치, 거리 저장
    dis = [[-1 for _ in range(n)] for _ in range(n)]  # 해당 좌표까지의 이동거리
    q = deque()
    q.append([y, x])
    dis[y][x] = 0

    while q:
        cur_y, cur_x = q.popleft()

        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]

            if (0 <= ny < n) and (0 <= nx < n):
                if board[ny][nx] <= size and dis[ny][nx] == -1:
                    dis[ny][nx] = dis[cur_y][cur_x] + 1
                    q.append([ny, nx])

                    # 먹을 수 있는 물고기 저장
                    if 0 < board[ny][nx] < size:
                        fish.append([ny, nx, dis[ny][nx]])

    fish.sort(key=lambda x: (x[2], x[0], x[1]))
    return fish

if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    n = int(input())
    board = []
    cur_y = 0
    cur_x = 0
    size = 2
    answer = 0
    cnt = 0

    for _ in range(n):
        board.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                cur_y = i
                cur_x = j

    while True:
        fish = bfs(cur_y, cur_x, size, n)
        if not fish:
            break

        y, x, dis = fish.pop(0)     # 이동
        board[cur_y][cur_x] = 0
        board[y][x] = 0
        cur_y, cur_x = y, x

        cnt += 1
        answer += dis

        if cnt == size:
            size += 1
            cnt = 0

    print(answer)
