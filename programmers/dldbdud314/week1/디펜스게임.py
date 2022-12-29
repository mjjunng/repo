# 50.0 / 100.0

def can_cross(n, k, check):
    cur_len = 0
    for x in sorted(check):  # ... maybe 시간초과?
        if n - x >= 0:
            n -= x
            cur_len += 1
    return cur_len + k


def solution(n, k, enemy):
    if len(enemy) <= k:
        return len(enemy)

    l, r = 0, len(enemy) - 1
    while l < r:
        m = (l + r) // 2
        check = enemy[0: m + 1]
        total_len = can_cross(n, k, check)
        if total_len < m:
            r = m
        else:
            l = m + 1

    return m


print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))