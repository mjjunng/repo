"""
틀린 풀이)

점화식: DP[n] = max(DP[1] * n, DP[n의약수1] * k, ..., P[k])

from math import ceil

# k의 약수 구하기 : 1부터 k의 제곱근까지 나누어지는 수 구하기
def get_divisors(k):
    res = set()
    for i in range(1, ceil(k ** 0.5) + 1):
        if k % i == 0:
            res.add(i)
            res.add(k // i)
    if k > 1:  # 1보다 큰 경우 자기자신 제외
        res.remove(k)
    return sorted(list(res))


n = int(input())
p = list(map(int, input().split()))

dp = [0] * (n + 1)
dp[1] = p[0]
for cnt in range(1, n + 1)
    divs = get_divisors(cnt)  # 약수 구하기
    div_dps = [dp[x] * (cnt // x) for x in divs]  # 약수 DP 모음
    div_dps.append(p[cnt - 1])
    dp[cnt] = max(div_dps)

print(dp[n])

# P1 = 3, P2 = 5, P3 = 15, P4 = 16 인 경우 통과 X -> 다른 카드팩끼리 조합 되는 경우
"""

"""
풀이 참고)

DP[i] = P[k] + DP[i - k] -> k번째 카드팩 가격(new!) + DP[i - k] 중 최대값
(DP[i] : 카드 i개 구매할 때 최대 가격)
"""
n = int(input())
p = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    for k in range(1, i + 1):
        dp[i] = max(dp[i], p[k] + dp[i - k])  # k번째 카드를 선택한 경우 + 기존 DP

print(dp[n])
