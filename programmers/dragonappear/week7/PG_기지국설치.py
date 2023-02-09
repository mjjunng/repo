# https://school.programmers.co.kr/learn/courses/30/lessons/12979
from math import ceil

"""
N의 범위가 2억이라 O(N)으로 풀이해야 한다
기지국 기준으로 왼쪽 공간부터 차례대로 처리하면 된다
"""


def solution(n, stations, w):
    answer = 0
    width = 2*w + 1
    start = 1

    for x in stations:
        dist = x - w - start
        if dist > 0:
            answer += ceil(dist / width)
        start = x + w + 1

    if n >= start:
        dist = n - start + 1
        answer += ceil(dist / width)

    return answer
