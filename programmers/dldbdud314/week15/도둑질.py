"""
** DP

- dp[i] = [i번째 안 훔쳤을 때 MAX, 훔친 경우 MAX] => 2개의 dp
- dp[i][0] = max(dp[i - 1]) -> 현재 안 훔친 경우 : 이전 꺼 상관없이 그대로
- dp[i][1] = dp[i - 1][0] + arr[i] -> 현재 훔친 경우
"""


def solution(money):
    # 첫번째 집 턴 경우 / 첫번째 집 안 턴 경우 (-> 마지막 요소 고려)
    dp1 = [[0, 0] for _ in range(len(money))]
    dp2 = [[0, 0] for _ in range(len(money))]
    dp1[0][1] = money[0]

    for i in range(1, len(money)):
        dp1[i][0] = max(dp1[i - 1])  # 현재 안 훔친
        if i != len(money) - 1:
            dp1[i][1] = dp1[i - 1][0] + money[i]  # 현재 훔친

        dp2[i][0] = max(dp2[i - 1])  # 현재 안 훔친
        dp2[i][1] = dp2[i - 1][0] + money[i]  # 현재 훔친

    res = max(max(dp1[-1]), max(dp2[-1]))

    return res
