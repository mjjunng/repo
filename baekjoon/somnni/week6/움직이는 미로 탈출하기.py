from collections import deque
dx = [0,0,1,-1,1,-1,1,-1,0]
dy = [1,-1,0,0,1,1,-1,-1,0]
n = 8


def solution():
    while q:
        x, y, t = q.popleft()
        if x == 0 and y == 7:
            return True
        for k in range(9):
            nx, ny = x+dx[k], y+dy[k]
            nt = min(t+1, 8)
            if 0 <= nx < n and 0 <= ny < n:
                if nx-t >= 0 and a[nx-t][ny] == '#':
                    continue
                if nx-t-1 >= 0 and a[nx-t-1][ny] == '#':
                    continue
                if not check[nx][ny][nt]:
                    check[nx][ny][nt] = True
                    q.append((nx,ny,nt))


a = [input() for _ in range(n)]
q = deque()
check = [[[False]*(n+1) for j in range(n)] for i in range(n)]
check[7][0][0] = True
q.append((7,0,0))
print(int(solution()))