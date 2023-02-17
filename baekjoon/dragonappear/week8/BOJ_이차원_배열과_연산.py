# https://www.acmicpc.net/problem/17140
from sys import stdin
from bisect import bisect_left, bisect_right
input = stdin.readline


def sorting(arr):
    arr.sort()

    s = set(arr)
    if 0 in s:
        s.remove(0)

    rst = []
    for a in list(s):
        lt = bisect_left(arr, a)
        rt = bisect_right(arr, a)
        rst.append([a, rt-lt])

    rst.sort(key=lambda x: (x[1], x[0]))
    tmp = []
    for r in rst:
        tmp.append(r[0])
        tmp.append(r[1])
    length = len(tmp)
    return (tmp+[0]*(101-length), length)


R, C, K = map(int, input().split())
board = [[0]*(101) for _ in range(101)]
for i in range(3):
    a = list(map(int, input().split()))
    board[i] = a + [0]*(98)

time = 0
tr, tc = 3, 3
escape = False
while True:
    if board[R-1][C-1] == K:
        break

    if time > 100:
        escape = True
        break

    if tr >= tc:
        for i in range(tr):
            rst = sorting(board[i])
            board[i] = rst[0]
            c = rst[1]
            tc = max(tc, c)
    else:
        for i in range(tc):
            tmp = [board[j][i] for j in range(101)]
            rst = sorting(tmp)
            tmp = rst[0]

            for j in range(101):
                board[j][i] = tmp[j]

            r = rst[1]
            tr = max(tr, r)

    time += 1

if escape:
    print(-1)
else:
    print(time)
