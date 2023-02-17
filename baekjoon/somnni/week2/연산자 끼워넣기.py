import math
n = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))

def solution(i, n, A, op, c):
    if i == n:
        if c < ans[1]:
            ans[1] = c
        if c > ans[0]:
            ans[0] = c
        return
    if op[0] > 0:
        solution(i+1, n, A, [op[0]-1,op[1],op[2],op[3]], c + A[i])
    if op[1] > 0:
        solution(i+1, n, A, [op[0],op[1]-1,op[2],op[3]], c - A[i])
    if op[2] > 0:
        solution(i+1, n, A, [op[0],op[1],op[2]-1,op[3]], c * A[i])
    if op[3] > 0:
        if c < 0:
            r = math.ceil(c / A[i])
        else:
            r = math.floor(c / A[i])
        solution(i+1, n, A, [op[0],op[1],op[2],op[3]-1], r)

ans = [-1000000000, 100000000]
solution(1, n, A, op, A[0])
print(ans[0])
print(ans[1])