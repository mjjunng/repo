"""
5549. 행성 탐사
** 누적합
쿼리별 :
- (0, 0) ~ (M, N)까지 누적합 구해서
- 주어진 시작 ~ 끝점에 따라 짤라서 계산
"""


def calc(sx, sy, ex, ey):
    res = [0, 0, 0]
    tmp1 = p_sum[sx - 2][ey - 1] if sx - 2 >= 0 else [0, 0, 0]
    tmp2 = p_sum[ex - 1][sy - 2] if sy - 2 >= 0 else [0, 0, 0]
    tmp3 = p_sum[sx - 2][sy - 2] if (sx - 2 >= 0 and sy - 2 >= 0) else [0, 0, 0]
    for k in range(3):
        res[k] = p_sum[ex - 1][ey - 1][k] - tmp1[k] - tmp2[k] + tmp3[k]
    return res


def add(s1, s2, s3, cur):
    return [s1[k] + s2[k] - s3[k] + cur[k] for k in range(3)]


def counter(cx, cy):
    if MAP[cx][cy] == 'J':
        return [1, 0, 0]
    elif MAP[cx][cy] == 'O':
        return [0, 1, 0]
    else:
        return [0, 0, 1]


m, n = map(int, input().split())
q = int(input())
MAP = [input() for _ in range(m)]

# 2차원 Prefix Sum
p_sum = [[[0, 0, 0] for _ in range(n)] for _ in range(m)]  # [J, O, I] 각각의 합
p_sum[0][0] = counter(0, 0)
for i in range(1, m):
    for k in range(3):
        p_sum[i][0][k] = p_sum[i - 1][0][k] + counter(i, 0)[k]
for j in range(1, n):
    for k in range(3):
        p_sum[0][j][k] = p_sum[0][j - 1][k] + counter(0, j)[k]

for i in range(1, m):
    for j in range(1, n):
        p_sum[i][j] = add(p_sum[i - 1][j], p_sum[i][j - 1], p_sum[i - 1][j - 1], counter(i, j))

print(*p_sum, sep='\n')

# 쿼리 돌면서 누적합 구하기
for _ in range(q):
    sx, sy, ex, ey = map(int, input().split())
    print(*calc(sx, sy, ex, ey))

