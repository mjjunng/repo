'''
17140. 이차원 배열과 연산
** 시뮬레이션, 구현 (풀이 일부 참고)

- R, C 연산 따로 구현 했다가 matrix 건드리지 않고는 유동적으로 열을 늘릴 수 없다는 걸 깨달음
- zip 연산 참고 (matrix transpose) -> R 연산만 구현
'''
from collections import Counter
from itertools import chain


def rc_calc(matrix, n):  # R 연산 + matrix trimming
    max_n = -float('inf')
    for i in range(n):  # 행별 sort
        target = [x for x in matrix[i] if x != 0]  # 0 제외 시키고 (->0까지 카운팅
        sorted_lst = sorted(Counter(target).items(), key=lambda x: (x[1], x[0]))
        matrix[i] = list(chain(*sorted_lst))  # 2차원 -> 1차원 -> 다시 해당 행에 담기

        max_n = max(max_n, len(matrix[i]))  # 최대 길이 tracking

    # 최대 행 길이에 맞춰 0 채우기
    for i in range(n):
        if len(matrix[i]) < max_n:
            matrix[i] = matrix[i] + [0] * (max_n - len(matrix[i]))
        matrix[i] = matrix[i][:100]


r, c, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(3)]

time = -1
for t in range(101):
    r_len, c_len = len(matrix), len(matrix[0])  # 세로 길이, 가로 길이
    if 0 < r <= r_len and 0 < c <= c_len and matrix[r - 1][c - 1] == k:
        time = t
        break

    # R 연산 / C 연산 (+ matrix trimming)
    if r_len >= c_len:
        rc_calc(matrix, r_len)
    else:
        matrix = list(map(list, zip(*matrix)))  # zip 활용 -> 행열 변환 (transpose)
        rc_calc(matrix, c_len)
        matrix = list(map(list, zip(*matrix)))  # 원상복귀

print(time)
