# https://www.acmicpc.net/problem/22968
from sys import stdin
from math import log2
from bisect import bisect_right
input = stdin.readline

MAX = int(log2(1000000000))*2
d = [0]*(MAX)
d[0], d[1], d[2] = 1, 2, 4
for i in range(3, MAX):
    d[i] = d[i-1]+d[i-2]+1

for _ in range(int(input())):
    n = int(input())
    print(bisect_right(d, n))

"""
DP

d(h) = 높이가 h인 AVL 트리 중 최소 노드 개수
d(0)=1
d(1)=2
d(2)=4
d(3)=7

-> d(h) = d(h-2)+d(h-1)+1
-> 높이가 H, 노드 개수가 N인 AVL 트리: H = O(logN)
"""
