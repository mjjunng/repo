"""
Greedy
time: 최악의 경우 -> 4 * n (n은 큐의 길이)

- 합이 같아질 때까지 큐1의 합 vs. 큐2의 합 비교 -> 연산
- 종료: 최대 [초기 길이 * 4]까지 -> 초기 리스트와 같아질 때까지의 연산 횟수
"""
from collections import deque


def solution(queue1, queue2):
    sum1, sum2 = sum(queue1), sum(queue2)
    if (sum1 + sum2) % 2 == 1:
        return -1
    count = 0
    queue1, queue2 = deque(queue1), deque(queue2)
    init_qlen = len(queue1)
    while sum1 != sum2:
        if count >= init_qlen * 4:
            return -1
        if sum1 > sum2:
            popped = queue1.popleft()
            sum1 -= popped
            queue2.append(popped)
            sum2 += popped
        else:
            popped = queue2.popleft()
            sum2 -= popped
            queue1.append(popped)
            sum1 += popped
        count += 1

    return count
