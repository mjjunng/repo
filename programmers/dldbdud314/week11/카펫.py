"""
** 두개의 방정식 활용한 완전 탐색
yellow 개수 = (x - 2) * (y - 2)
brown 개수 = 2 * x + 2 * y - 4

- 두 방정식 제일 처음 만족하는 w, h에 대해 RETURN [w, h] (가로 >= 세로 => 그리디)
"""


def solution(brown, yellow):
    h = 1  # 세로 길이
    while True:
        # 1차 방정식 만족하는 w, h에 대해
        if (brown - 2 * h + 4) % 2 != 0:  # 1. brown 조건 통과 ?
            continue

        w = (brown - 2 * h + 4) // 2  # 가로 길이 정해짐
        if (w - 2) * (h - 2) == yellow:  # 2. yellow 조건 통과 ?
            return [w, h]
        h += 1
