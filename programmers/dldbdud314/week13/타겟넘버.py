"""
** BFS 완전 탐색
"""
from collections import deque


def solution(numbers, target):
    queue = deque([0])

    for i in range(len(numbers)):
        num = numbers[i]
        for _ in range(2 ** i):
            cur = queue.popleft()

            queue.append(cur - num)
            queue.append(cur + num)

    return queue.count(target)  # 마지막 숫자까지 처리한 결과가 큐에 들어가 있음
