"""
1927. 최소힙

** 최소힙 기본
"""
from heapq import heappop, heappush
import sys
input = sys.stdin.readline


n = int(input())

heap = []
for _ in range(n):
    x = int(input())
    if x > 0:
        heappush(heap, x)
    else:
        print(heappop(heap)) if heap else print(0)
