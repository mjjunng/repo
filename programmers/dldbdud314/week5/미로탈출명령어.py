"""
통과X
카카오 해설 참고: https://tech.kakao.com/2023/01/25/2023-kakao-recruitment-round-1/
"""
from bisect import bisect_right


def solution(n, m, x, y, r, c, k):
    # (최단 거리 > k)이거나 (k - 최단 거리) % 2 == 1인 경우 -> impossible
    min_len = abs(x - r) + abs(y - c)
    if min_len > k or (k - min_len) % 2 == 1:
        return "impossible"

    # 그리디 하게 탐색 순서 배치 !
    # 'd' > 'l' > 'rl' > 'r' > 'u'순의 배치가 최적이라는 점을 이용
    path = ''  # 최단 경로 먼저 만들기
    if x <= r:  # 'd' 먼저, 'l'/'r' 그 다음
        path = 'd' * (r - x) + ('l' * (y - c) if y >= c else 'r' * (c - y))
    else:  # 'l'/'r' 먼저, 'u'는 그 다음
        path += ('l' * (y - c) if y >= c else 'r' * (c - y)) + 'u' * (x - r)

    # 'k > 최단거리'인 경우, 경우를 나눠서 'rl' 끼워 넣기
    if k > len(path):
        to_add = (k - len(path)) // 2
        if set(path) == {'d', 'l'}:   # 'd' -> 'l' -> 'rl'
            path += 'rl' * to_add
        elif set(path) == {'d', 'r'}:
            idx = bisect_right(path, 'd')  # 'd' -> 'rl' -> 'r'
            path = path[:idx] + 'rl' * to_add + path[idx:]
        elif set(path) == {'l', 'u'}:
            idx = bisect_right(path, 'l')  # 'l' -> 'rl' -> 'r'
            path = path[:idx] + 'rl' * to_add + path[idx:]
        elif set(path) == {'r', 'u'}:  # 'rl' -> 'r' -> 'u'
            path = 'rl' * to_add + path[:]

    return path


# print(solution(3, 4, 2, 3, 3, 1, 5))  # 'dllrl'
print(solution(2, 2, 1, 1, 2, 2, 6))  # 'dr'
