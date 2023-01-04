n = int(input())
weights = list(map(int, input().split()))
m = int(input())
marbles = list(map(int, input().split()))

dp = [[False] * 40001 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(max(marbles) + 1):
        if j == 0:
            dp[i][j] = True
            continue
        w = weights[i - 1]
        dp[i][j] = dp[i - 1][abs(j - w)] or dp[i - 1][j + w] or dp[i - 1][j]

for marble in marbles:
    if dp[n][marble]:
        print('Y', end=' ')
    else:
        print('N', end=' ')