"""
5549. 행성 탐사
** 누적합
쿼리별 :
- (0, 0) ~ (M, N)까지 누적합 구해서
- 주어진 시작 ~ 끝점에 따라 짤라서 계산
"""
import sys
input = sys.stdin.readline


def calc(sx, sy, ex, ey):
    res = [0, 0, 0]
    for k in range(3):
        res[k] = p_sum[ex][ey][k] - p_sum[sx - 1][ey][k] - p_sum[ex][sy - 1][k] + p_sum[sx - 1][sy - 1][k]
    return res


# 하나의 칸 구하기 -> 'J', 'O', 'I' 각각 연산해서 return
def add(s1, s2, s3, cur):
    return [s1[k] + s2[k] - s3[k] + cur[k] for k in range(3)]


# 해당 영역 구분하기
def counter(key):
    return {'J': [1, 0, 0], 'O': [0, 1, 0], 'I': [0, 0, 1]}.get(key)


m, n = map(int, input().split())
q = int(input())
MAP = [input() for _ in range(m)]

# 2차원 Prefix Sum -> (n + 1) * (m + 1) 공간으로 수정
p_sum = [[[0, 0, 0] for _ in range(n + 1)] for _ in range(m + 1)]  # ['J', 'O', 'I'] 각각의 합
for i in range(m):
    for j in range(n):
        p_sum[i + 1][j + 1] = add(p_sum[i][j + 1], p_sum[i + 1][j], p_sum[i][j], counter(MAP[i][j]))

# 쿼리 돌면서 누적합 구하기
for _ in range(q):
    sx, sy, ex, ey = map(int, input().split())
    print(*calc(sx, sy, ex, ey))

