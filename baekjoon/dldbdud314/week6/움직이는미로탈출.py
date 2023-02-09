"""
백준 16954. 움직이는 미로 탈출

<< BFS + 시뮬레이션(구현) >>
- 상하좌우, 대각선 포함해서 다음 이동할 수 있는 모든 장소 큐에 저장
- 벽 아래로 한칸씩 이동하여 MAP 업데이트
- 오른쪽 위 도달하면 1 return

MISSED:
a. 현재 위치에 서있는 경우 빼먹음
b. 잘못된 벽 이동 함수 작성
c. 방문 처리 문제 (참고: https://www.acmicpc.net/board/view/84407)

** 의외로 방문 처리 가장 중요한 문제,, 더 생각해봐야 한다!
"""
from collections import deque

# 필요한 상수 목록
dirs = [(-1, 1), (0, 1), (-1, 0), (1, 1), (-1, -1), (1, 0), (0, -1), (1, -1), (0, 0)]  # 현재 위치에 서 있는 경우도 포함!
n = 8  # 체스판의 한 변 길이
EMPTY, WALL = '.', '#'  # 빈칸, 벽


# 벽 아래로 한칸씩 이동
def move_walls(old_MAP):
    new_MAP = [[EMPTY] * n]
    for line in range(0, n - 1):  # 맨 아랫줄 제외 추가
        new_MAP.append(old_MAP[line])
    return new_MAP


def all_empty():  # 전부 다 빈칸인 경우 판별
    cnt = 0
    for i in range(n):
        cnt += MAP[i].count(EMPTY)
    return cnt == n * n


MAP = [list(input()) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
queue = deque([(n - 1, 0, 0)])  # x, y, t

cur_time = 0  # 사용자 한 칸 이동 tracking 용도

success = False  # 이동 가능한지 결과 Flag
while queue:
    cx, cy, t = queue.popleft()

    if cx == 0 and cy == n - 1:  # 목표 지점 도달 가능한 경우 BREAK
        success = True
        break

    # 사용자 한칸 이동한 경우
    if cur_time + 1 == t:
        MAP = move_walls(MAP)  # 이동 위치 갱신
        cur_time += 1
        if all_empty():  # 벽이 사라진 경우
            success = True
            break

    if MAP[cx][cy] == WALL:  # 현재 위치에 벽이 내려 앉은 경우 무효화
        continue

    visited[cx][cy] = True  # 방문 처리

    for dx, dy in dirs:
        if (dx, dy) == (0, 0):  # 현재 위치에 서 있는 경우 따로 처리
            queue.append((cx, cy, t + 1))
        elif 0 <= cx + dx < n and 0 <= cy + dy < n and MAP[cx + dx][cy + dy] == EMPTY and not visited[cx + dx][cy + dy]:
            queue.append((cx + dx, cy + dy, t + 1))

print(int(success))
