# dfs 
# 처음 dfs를 시작한 위치와 끝 위치가 같다면 사이클! 

import sys

def dfs(y, x, visited, cnt, s_y, s_x):
    global flg

    if flg: # 이미 사이클을 찾았다면 더이상 탐색X
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if (0 <= ny < n) and (0 <= nx < m):
            if board[ny][nx] == board[y][x]:  # 색이 같고 
                if visited[ny][nx] == 0:      # 방문을 하지 않았을 때만 dfs 탐색 
                    visited[ny][nx] = 1
                    dfs(ny, nx, visited, cnt+1, s_y, s_x)
                else:
                    if ny == s_y and nx == s_x: # 색이 같고, 시작 위치와 탐색하려는 위치가 같고 
                        if cnt+1 >= 4:          # 탐색한 칸이 4이상이라면, 사이클!!
                            flg = True



if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    n, m = map(int, input().split())
    board = []
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    for _ in range(n):
        board.append(list(input()))

    for i in range(n):
        for j in range(m):
            visited = [[0 for _ in range(m)] for _ in range(n)]
            flg = False
            visited[i][j] = 1
            dfs(i, j, visited, 0, i, j)
            if flg:
                print("Yes")
                break

        if flg:
            break

    if not flg:
        print("No")

