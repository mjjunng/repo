"""
22968. 균형 - 풀이 참고

** DP
- dp[h] = dp[h-1] + dp[h-2] + 1
- dp[h] : 높이가 h인 트리의 최대 노드 개수
"""
import sys
from bisect import bisect_right
input = sys.stdin.readline


# 최소 노드 개수로 만들 수 있는 최대 높이 -> dp[h] = n (h = 높이, n = 노드 개수)
dp = [1, 2]
while True:
    dp.append(dp[-1] + dp[-2] + 1)
    if dp[-1] > 1_000_000_000:
        dp.pop()
        break

t = int(input())
for _ in range(t):
    v = int(input())
    print(bisect_right(dp, v))
