"""
구현
1. 중복 조합을 활용해 라이언이 가질 수 있는 모든 점수 조합을 구하기
2. 가장 큰 점수 차이(라이언 총 점수 - 어피치 총 점수) 구하기
3. 가장 점수 차이가 크고 낮은 점수가 우선 순위 높도록 점수 배열 갱신
    - 해당 연산의 편의성을 위해 점수 배열 역순 배치하여 비교
"""
from itertools import combinations_with_replacement


# 총 점수 차이 계산
def get_score_diff(apeach_info, lion_info):
    apeach_total, lion_total = 0, 0
    score = 0
    for acnt, rcnt in zip(apeach_info, lion_info):
        if acnt == rcnt == 0:
            score += 1
            continue
        if acnt >= rcnt:
            apeach_total += score
        else:
            lion_total += score
        score += 1

    return lion_total - apeach_total if lion_total > apeach_total else 0


# 중복 조합 활용
def solution(n, info):
    max_score_diff = -float('inf')  # 가장 큰 점수 차
    max_score_info = []  # 가장 큰 점수 차일 때, 라이언의 점수 배열 기록 (max_score가 같은 경우, 비교해서 갱신)
    for combi in combinations_with_replacement(range(11), n):
        lion_info = [0] * 11
        for idx in combi:
            lion_info[idx] += 1  # 라이언이 맞힌 점수 배열 -> 비교 연산의 편의를 위해 0점 ~ 10점 순

        cur_score_diff = get_score_diff(list(reversed(info)), lion_info)
        if cur_score_diff > 0 and cur_score_diff > max_score_diff:
            max_score_diff = cur_score_diff
            max_score_info = lion_info
        elif max_score_diff == cur_score_diff:
            max_score_info = max(max_score_info, lion_info)

    return [-1] if max_score_diff == -float('inf') else list(reversed(max_score_info))


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
