"""
1st) 시간 초과
Brute force: 시작점 (x, y)에 대해 한 변의 길이 n을 설정해가며 가장 큰 정사각형 크기 구하기 -> 최악의 경우 O(1000*1000*1000)로 시간 초괴

2nd) 풀이 참고 -> DP
- DP[i][j] : 최대 변 길이
- 현재 인덱스 (i, j)에 대해 (i-1, j), (i-1, j-1), (i, j-1) 중 최소값 + 1
"""

n, m = map(int, input().split())
MAP = [list(map(int, list(input()))) for _ in range(n)]

# DP 순회하며 최대 길이 구하기
dp = [[0] * m for _ in range(n)]
max_len = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0 or MAP[i][j] == 0:  # 예외 처리
            dp[i][j] = MAP[i][j]
        elif i > 0 and j > 0 and MAP[i][j] == 1:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        max_len = max(dp[i][j], max_len)

print(max_len * max_len)
