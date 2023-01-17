import sys
from collections import deque


'''
    bfs: 실패 
     
'''

def bfs(sy, sx, ey, ex):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    q = deque() # [y좌표, x좌표, 방향]
    visited = [[float('inf') for _ in range(n)] for _ in range(m)]
    visited[sy][sx] = 0 # visited[y][x]: y, x 에서의 최소 거울 개수

    # 처음 동서남북 이동 가능한 경로 초기화
    for i in range(4):
        ny = sy + dy[i]
        nx = sx + dx[i]

        if (0 <= ny < m) and (0 <= nx < n) and board[ny][nx] != '*':
            q.append([ny, nx, i])
            visited[ny][nx] = 0

    while q:
        y, x, dir = q.popleft()
        print("now sibal ", y, x)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if (0 <= ny < m) and (0 <= nx < n) and board[ny][nx] != '*':
                # 이전과 같은 방향이라면 거울 늘리지 않아도 됨
                mirror = visited[y][x]
                if i != dir:    # 이전과 다른 방향이라면 꺾어야 하기 때문에 거울 1개 추가
                    mirror += 1

                # 최솟값으로 갱신
                if visited[ny][nx] > mirror:
                    visited[ny][nx] = mirror
                    q.append([ny, nx, i])
    return visited[ey][ex]

if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    n, m = map(int, input().split())
    board = []
    pos = []

    for i in range(m):
        board.append(list(input()))
        for j in range(n):
            if board[i][j] == 'C':
                pos.append([i, j])

    print(bfs(pos[0][0], pos[0][1], pos[1][0], pos[1][1]))
