"""
O(n)..?! -> 끝에서부터 cap에 맞게 배달/수거, 상황에 맞게 이동거리 업데이트 !
1st try: fail..~
"""


def solution(cap, n, deliveries, pickups):
    moved = 0
    delivered, picked = 0, 0
    idx = n - 1
    while idx > -1:
        # edge case
        if deliveries[idx] == 0:  # 수거할 게 있어야 !
            idx -= 1
            continue

        # cap만큼 배달하기
        i = idx  # 배달이 끝나는 지점 -> 이걸 기준으로 이동거리 update
        while i >= 0 and delivered < cap:
            if delivered + deliveries[i] <= cap:
                delivered += deliveries[i]
                deliveries[i] = 0
            else:
                delivered = cap
                deliveries[i] = delivered + deliveries[i] - cap
            i -= 1

        # delivered == cap -> idx(배달이 끝난 지점)부터 수거 시작
        j = idx
        while j >= 0 and picked < cap:
            if picked + pickups[j] <= cap:
                picked += pickups[j]
                pickups[j] = 0
            else:
                picked = cap
                pickups[j] = picked + pickups[j] - cap
            j -= 1

        # 다음에 배달 시작할 지점(->idx) update
        moved += (idx + 1) * 2
        delivered, picked = 0, 0
        idx = i + 1

    return moved


# print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
