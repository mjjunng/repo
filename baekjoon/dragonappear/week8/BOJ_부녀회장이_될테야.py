# https://www.acmicpc.net/problem/2775
from sys import stdin
input = stdin.readline

"""
dp
"""


def solve():
    K = int(input())
    N = int(input())

    # d[k][i] : k층 i호 인원 수
    # d[k-1][1] + ... + d[k-1][i]
    d = [[0]*(N+10) for _ in range(K+10)]
    for i in range(N+1):
        d[0][i] = i

    for k in range(1, K+1):
        for i in range(1, N+1):
            s = 0
            for j in range(1, i+1):
                s += d[k-1][j]
            d[k][i] = s

    print(d[K][N])


for _ in range(int(input())):
    solve()
