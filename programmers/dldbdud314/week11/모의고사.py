"""
** 구현
- 각 수포자 찍는 패턴 저장, 정답 돌면서 모듈러와 일치할 경우 점수++
"""


def solution(answers):
    # 찍는 패턴
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0] * 3  # 1, 2, 3번 수포자 점수
    for i in range(len(answers)):
        if one[i % 5] == answers[i]:
            scores[0] += 1
        if two[i % 8] == answers[i]:
            scores[1] += 1
        if three[i % 10] == answers[i]:
            scores[2] += 1
    max_score = max(scores)  # 제일 큰 점수

    return [i + 1 for i in range(3) if scores[i] == max_score]
