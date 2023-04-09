"""
** DP (+ 그리디 아이디어)

1st) dfs top-down -> FAIL 33.3 / 100.0
2nd) 반복문 bottom-up -> SUCCESS
- 경계값 처리에서 허우적
- 중복 연산으로 효율성 ALL FAIL -> vis 처리
"""
INF = int(1e9)


def solution(arr):
    operator, operands = [], []  # 연산자, 피연산자 모음
    for x in arr:
        if x.isdigit():
            operands.append(int(x))
        else:
            operator.append(x)
    n = len(operands)

    min_dp = [[INF] * n for _ in range(n)]
    max_dp = [[-INF] * n for _ in range(n)]
    vis = [[False] * n for _ in range(n)]  # 중복 연산 방지
    for i in range(n):
        min_dp[i][i] = operands[i]
        max_dp[i][i] = operands[i]
        vis[i][i] = True

    # bottom-up
    for cnt in range(2, n + 1):
        for i in range(0, n - cnt + 1):
            for j in range(i + 1, i + cnt):
                if vis[i][j]:
                    continue
                vis[i][j] = True

                for k in range(cnt - 1):
                    if operator[i + k] == '-':
                        min_dp[i][j] = min(min_dp[i][i + k] - max_dp[i + k + 1][j], min_dp[i][j])
                        max_dp[i][j] = max(max_dp[i][i + k] - min_dp[i + k + 1][j], max_dp[i][j])
                    else:
                        min_dp[i][j] = min(min_dp[i][i + k] + min_dp[i + k + 1][j], min_dp[i][j])
                        max_dp[i][j] = max(max_dp[i][i + k] + max_dp[i + k + 1][j], max_dp[i][j])

    return max_dp[0][n - 1]
