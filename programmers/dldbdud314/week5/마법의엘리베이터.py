# Greedy + BFS - 잘못된 접근 -> FAIL
from collections import deque


def solution0(storey):
    queue = deque([(storey, 0)])
    min_cnt = float('inf')
    while queue:
        s, cnt = queue.popleft()
        print(s, cnt)

        if s == 0:
            min_cnt = min(min_cnt, cnt)
            continue

        unit = 10 ** len(str(abs(s)))  # 10의 제곱 상한선

        tmp = int(str(abs(s))[0])
        if s > 0:
            queue.append((s - tmp * unit, cnt + tmp))
            if s - tmp * unit != 0:
                queue.append((s - (tmp + 1) * unit, cnt + tmp + 1))
        else:
            queue.append((s + tmp * unit, cnt + tmp))
            if s + tmp * unit != 0:
                queue.append((s + (tmp + 1) * unit, cnt + tmp + 1))

    return min_cnt


# BFS로 모든 경우의 수 따져 보기 (자릿수 별 올림 or 내림) -> O(2 ** 자릿수)
def solution(storey):
    queue = deque([(storey, 0)])
    min_cnt = float('inf')  # 최소 누른 횟수 갱신
    visited = set()  # 해당 층 방문 여부
    while queue:
        s, cnt = queue.popleft()  # 층, 버튼 누른 횟수

        if s == 0:
            min_cnt = min(cnt, min_cnt)
            continue

        visited.add(s)

        first = s % 10  # 일의 자릿수 짜르기
        if (s // 10) not in visited:  # 이미 처리한 수가 아니면 큐에 추가
            queue.append((s // 10, cnt + first))  # 내림
        if (s // 10 + 1) not in visited:
            queue.append((s // 10 + 1, cnt + 10 - first))  # 올림

    return min_cnt


print(solution(5555))
print(solution(57595358))
