# https://school.programmers.co.kr/learn/courses/30/lessons/131704
from collections import deque


def solution(order):
    ans = 0
    N = len(order)
    stack = []

    belt = deque([i for i in range(1, N + 1)])

    while ans < N:

        if belt and order[ans] == belt[0]:
            ans += 1
            belt.popleft()
        elif stack and order[ans] == stack[-1]:
            ans += 1
            stack.pop()
        elif stack and order[ans] < stack[-1]:
            break
        elif belt:
            stack.append(belt.popleft())

    return ans


print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))
