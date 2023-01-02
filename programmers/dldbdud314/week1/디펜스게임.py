# parametric search
# 62.5 / 100.0
def can_cross(n, k, check):
    cur_len = 0
    for x in sorted(check):
        if n - x >= 0:
            n -= x
            cur_len += 1
    return cur_len + k


def solution2(n, k, enemy):
    if len(enemy) <= k:
        return len(enemy)

    l, r = 0, len(enemy) - 1
    while l < r:
        m = (l + r) // 2
        check = enemy[0: m]
        total_len = can_cross(n, k, check)
        if total_len < m:
            r = m
        else:
            l = m + 1

    return m


# heapq 활용 - 풀이 참고
from heapq import heappush, heappop


def solution(n, k, enemy):
    queue = []
    for rnd, x in enumerate(enemy):
        heappush(queue, x)

        if len(queue) > k:
            n -= heappop(queue)

        if n < 0:
            return rnd

    return len(enemy)


print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
print(solution(2, 4, [3, 3, 3, 3]))
