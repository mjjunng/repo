"""
O(n^2)이 아닌 접근 방식 안 떠올라서 풀이 참고
-> sort(key = lambda x: (-x[0], x[1])) 하고 비교
48.0 / 100.0 FAIL

수정: 완호 기준 점수 높은 사람 카운트
76.0 / 100.0 FAIL
"""


def solution(scores):
    # 완호 점수
    wh = scores[0]
    wh_sum = sum(scores[0])
    scores = scores[1:]  # 완호 제외
    # 인센티브 못 받는 사람 가리기 위해
    scores.sort(key=lambda x: (-x[0], x[1]))

    # 완호가 인센 못 받는지
    # 받는다면 본인보다 점수 크고 && 인센 받는 사람 기준 RANKING
    s1, s2 = -1, -1  # 인센 확인용 이전 점수 저장
    rank = 1
    for score in scores:
        if wh[0] < score[0] and wh[1] < score[1]:
            return -1
        if s1 > score[0] and s2 > score[1]:  # 인센X -> 쓰루
            s1, s2 = score[0], score[1]
            continue
        if score[0] + score[1] > wh_sum:  # 완호보다 점수 높은 사람 카운트
            rank += 1
        s1, s2 = score[0], score[1]

    return rank


print(solution([[3, 1], [1, 4], [2, 3], [2, 3], [1, 5], [1, 0], [1, 0]]))
