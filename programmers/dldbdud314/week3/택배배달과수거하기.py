"""
Greedy : stack 활용 (-> 끝에서부터 택배 처리 하기 때문에 스택 활용!)

풀이:
1. deliveries, pickups를 돌며 스택을 만든다 -> delivery_stack, pickup_stack
2. 배달과 수거
    - 최대한 cap만큼 배달/수거 후, 최장점(max_len) 업데이트
    - 전부 다 배달/수거하지 못하는 경우, 도로 stack에 append (남은 택배)
3. 이동거리 정보 갱신하기 (moved) -> 최장점(max_len) * 2

----
초기에 잘못 생각한 지점:
- 배달/수거 사이클의 최장점이 기준이 되어야 !
- 무조건 cap을 채운다는 보장이 없음 !
"""


def solution(cap, n, deliveries, pickups):
    delivery_stack, pickup_stack = [], []  # 앞-끝 순서로 [인덱스, 개수] 정보 저장
    for i in range(n):
        if deliveries[i] > 0:
            delivery_stack.append([i, deliveries[i]])
        if pickups[i] > 0:
            pickup_stack.append([i, pickups[i]])

    moved = 0  # 이동거리
    delivered, picked = 0, 0
    max_len = -float('inf')  # 이동거리 갱신을 위한 거리 정보 (한 사이클 당 이동거리의 최장점)
    while delivery_stack or pickup_stack:
        # 배달하기 (최대한 cap만큼)
        while delivered < cap and delivery_stack:
            dIdx, dCnt = delivery_stack.pop()
            if delivered + dCnt <= cap:
                delivered += dCnt
            else:
                delivery_stack.append([dIdx, delivered + dCnt - cap])
                delivered = cap
            max_len = max(max_len, dIdx)

        # 수거하기 (최대한 cap만큼)
        while picked < cap and pickup_stack:
            pIdx, pCnt = pickup_stack.pop()
            if picked + pCnt <= cap:
                picked += pCnt
            else:
                pickup_stack.append([pIdx, picked + pCnt - cap])
                picked = cap
            max_len = max(max_len, pIdx)

        # 배달/수거(하나의 이동 사이클) 끝 -> 거리 정보 업데이트
        delivered, picked = 0, 0
        if max_len == -float('inf'):
            break
        moved += (max_len + 1) * 2
        max_len = -float('inf')

    return moved


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))  # A: 16
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))  # A: 30
print(solution(2, 2, [0, 0], [0, 4]))  # A: 8
