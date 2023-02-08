# https://school.programmers.co.kr/learn/courses/30/lessons/152995
# https://sundryy.tistory.com/109
from typing import List
"""
N 범위: [1,10만] -> O(nlogn)

인센티브를 받지 못하는 사람은 걸러야 함
근무태도 점수가 높았던 그룹의 동료 평가 점수의 최댓값보다 작은 사람은 거름
"""


def solution(scores: List):
    ans = 1
    target = scores[0]
    tot = sum(target)
    # 근무태도 내림차순, 동료평가 오름차순 정렬
    # O(nlogn)
    scores.sort(key=lambda x: (-x[0], x[1]))

    thresh = -1
    for score in scores:  # O(n)
        if target[0] < score[0] and target[1] < score[1]:
            return -1
        if thresh <= score[1]:
            if tot < sum(score):
                ans += 1
            thresh = score[1]
    return ans


scores = [[2, 2], [1, 4], [3, 2], [3, 2], [2, 1]]
print(solution(scores))
