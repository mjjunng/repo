"""
O(n^2)이 아닌 접근 방식 안 떠올라서 풀이 참고
-> sort(key = lambda x: (-x[0], x[1])) 하고 비교

48.0 / 100.0
"""


def solution(scores):
    scores = list(map(tuple, scores))
    wh = scores[0]  # 원호 점수 저장
    scores.sort(key=lambda x: (-x[0], x[1]))

    # 인센티브 못 받는 점수 제거
    to_remove = set()  # 인센티브 못 받는 점수 목록
    for i in range(1, len(scores)):
        a1, b1 = scores[i - 1]
        a2, b2 = scores[i]
        if a1 > a2 and b1 > b2:
            to_remove.add(scores[i])

    if wh in to_remove:  # 원호가 인센 못 받는 경우
        return -1

    scores = [score for score in scores if score not in to_remove]  # 제거하고

    # RANKING - 동석차 고려
    scores = sorted(scores, key=lambda x: -sum(x))  # 합 기준 내림차순 정렬
    cur_rank = 1
    if scores[0] == wh:
        return cur_rank
    for i in range(1, len(scores)):
        sum1 = sum(scores[i - 1])
        sum2 = sum(scores[i])
        if sum1 > sum2:
            cur_rank = i + 1
        if scores[i] == wh:  # 원호 점수인 경우
            return cur_rank


print(solution([[3, 1], [1, 4], [2, 3], [2, 3], [1, 5], [1, 0], [1, 0]]))
