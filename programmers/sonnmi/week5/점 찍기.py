import math


def solution(k, d):
    answer = 0
    # 원의 방정식 이용
    d_square = d * d
    for i in range(0, d + 1, k):
        answer += math.sqrt(d_square-i*i) // k + 1
    return answer