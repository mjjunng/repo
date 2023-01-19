"""
DP, bottom-up 방식
- dp[i]: i일까지 벌 수 있는 최대 수익
"""

n = int(input())
t, p = [0] * n, [0] * n  # 날짜별 시간, 수익
for i in range(n):
    t[i], p[i] = map(int, input().split())

dp = [0] * (n + 1)
for i in range(n):  # i일의 상담을 한다고 했을 때
    for j in range(i + t[i], n + 1):  # 가능한 날짜 범위면 최대 수익 갱신
        if dp[j] < p[i] + dp[i]:
            dp[j] = p[i] + dp[i]

print(dp[-1])
