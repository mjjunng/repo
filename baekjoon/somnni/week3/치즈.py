from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
cnt = 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def bfs():
    de = deque()
    de.append([0, 0])
    c = [[-1] * m for _ in range(n)]
    c[0][0] = 0
    while de:
        print(de)
        y, x = de.popleft()
        for k in range(4):
            i = y + dy[k]
            j = x + dx[k]
            if 0 <= i < n and 0 <= j < m:
                print((i,j), end=" ")
                if c[i][j] == -1:
                    if a[i][j] >= 1:
                        a[i][j] += 1
                    else:
                        c[i][j] = 0
                        de.append([i, j])
        print()

while True:
    bfs()
    cht = False
    for i in range(n):
        for j in range(m):
            print(a[i][j], end=" ")
        print()
    for i in range(n):
        for j in range(m):
            if a[i][j] >= 3:
                a[i][j] = 0
                cht = True
            elif a[i][j] == 2:
                a[i][j] = 1
    if cht:
        cnt += 1
    else:
        break
print(cnt)