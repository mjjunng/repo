"""
** 스택/큐  (처음 문제 이해가 어려웠음,,)
- 자료구조 :
    - main (1 ~ n까지 queue)
    - sec (보조 벨트, stack, 즉 큰 수를 먼저 뺼 수 있는 구조)
- order 돌면서:
    - main이나 sec의 첫번째 요소와 일치 -> pop, cnt++
    - 일치하지 않는 경우 : 탐색 중간 / 계속할수도
"""
from collections import deque


def solution(order):
    last = len(order)  # 마지막 번호

    main = deque([i for i in range(1, last + 1)])  # 순서대로 들어간 메인 컨베이어 (큐)
    sec = []  # 보조 컨베이어 벨트 (스택)

    cnt = 0  # 실을 수 있는 상자 수
    p = 0  # order의 현재 포인터
    while p < last:
        # 메인 아니면 보조 첫번째 요소와 일치하는 경우
        if main and order[p] == main[0]:
            main.popleft()
            p += 1
            cnt += 1
            continue
        if sec and order[p] == sec[-1]:
            sec.pop()
            p += 1
            cnt += 1
            continue

        # 일치하지 않는 경우 -> 더 이상 탐색 불가능 / 더 탐색할 수 있음
        if main[0] < order[p]:  # 더 탐색할 수 있음 (main -> sec)
            sec.append(main.popleft())
        elif (main and order[p] < main[0]) and (sec and order[p] < sec[-1]):  # 탐색 불가
            break

    return cnt

