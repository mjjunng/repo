import sys

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def dfs(y, x, sum, cnt):
    global answer
    if cnt == 4:
        answer = max(answer, sum)
        return

    for i in range(len(dy)):
        ny = y + dy[i]
        nx = x + dx[i]

        if (0 <= ny < n) and (0 <= nx < m) and visited[ny][nx] == 0:
            visited[ny][nx] = 1
            dfs(ny, nx, sum+board[ny][nx], cnt+1)
            visited[ny][nx] = 0

def calc(y, x):
    global answer

    # ㅗ
    if y - 1 >= 0 and x + 1 < m and 0 <= x-1:
        tmp = board[y][x] + board[y][x-1] + board[y][x+1] + board[y - 1][x]
        answer = max(answer, tmp)

    # ㅜ
    if y + 1 < n and x + 1 < m and 0 <= x-1:
        tmp = board[y][x] + board[y][x-1] + board[y][x+1] + board[y + 1][x]
        answer = max(answer, tmp)

    # ㅏ
    if y + 1 < n and 0 <= y-1 and x+1 < m:
        tmp = board[y][x] + board[y - 1][x] + board[y + 1][x] + board[y][x + 1]
        answer = max(answer, tmp)

    # ㅓ
    if 0 <= y-1 and y+1 < n and 0 <= x-1:
        tmp = board[y][x] + board[y-1][x] + board[y][x-1] + board[y+1][x]
        answer = max(answer, tmp)


if __name__ == "__main__":
    n, m = map(int, input().split())
    answer = 0
    board = []
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(n):
        board.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(m):
            visited[i][j] = 1
            dfs(i, j, board[i][j], 1)
            visited[i][j] = 0

            calc(i, j)

    print(answer)
