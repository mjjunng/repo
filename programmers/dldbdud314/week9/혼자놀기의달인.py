"""
** 시뮬레이션 (구현)
총 두 번의 라운드를 거치면 된다
각각의 라운드 시작 카드를 combinations로 두 장 고른 뒤, 카드 선택 과정 진행
"""

from itertools import combinations


def solution(cards):
    n = len(cards)
    max_score = 0
    for first, scnd in combinations(range(n), 2):
        visited = set()  # 연 상자 목록
        # 첫번째 라운드 선택
        now1 = first  # 선택한 상자 인덱스
        cnt1, cnt2 = 0, 0
        for _ in range(n):
            if now1 in visited:
                cnt1 = len(visited)
                break
            visited.add(now1)
            now1 = cards[now1] - 1  # 다음 상자 인덱스 갱신
        # 첫번째 라운드에서 다 뽑거나 두번째 카드가 이미 고른 카드인 경우 PASS
        if cnt1 == n or scnd in visited:
            continue

        # 두번째 라운드 선택
        visited.clear()
        now2 = scnd  # 선택한 상자 인덱스
        for _ in range(n):
            if now2 in visited:
                cnt2 = len(visited)
                break
            visited.add(now2)
            now2 = cards[now2] - 1  # 다음 상자 인덱스 갱신

        if max_score < cnt1 * cnt2:
            max_score = cnt1 * cnt2

    return max_score
