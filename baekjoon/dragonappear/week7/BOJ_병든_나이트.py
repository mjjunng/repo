# https://www.acmicpc.net/problem/1783
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

if N == 1:
    print(1)
elif N == 2:
    print(min(4, (M-1)//2 + 1))
elif M < 7:
    print(min(4, M))
else:
    print((2 + (M-5)) + 1)
