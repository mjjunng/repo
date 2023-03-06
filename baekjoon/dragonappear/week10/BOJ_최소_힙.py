# https://www.acmicpc.net/problem/1927
from heapq import heappush, heappop
from sys import stdin
input = stdin.readline

heap = []
for _ in range(int(input())):
    n = int(input())
    if n:
        heappush(heap, n)
    else:
        if heap:
            print(heappop(heap))
        else:
            print(0)
