"""
백준 19236. 청소년 상어
풀이 참고 - 백트래킹

<< 시뮬레이션(구현) >>
- 자료구조:
    - fishes -> [x, y, d] 저장, 먹혔으면 삭제
    - MAP -> 물고기 위치 기록 (1 ~ 16 - 물고기 / 0 - 없음)
- 메인 로직 : DFS Backtracking
    - 전처리: MAP, fishes 복사본 만들기 (->Backtracking 때문에 임시 자료구조 필요)
    - 해당 위치의 물고기 잡아 먹기
    - 물고기 대이동
    - 상어 이동 -> 가능한 위치 후보군에 대해 DFS 재귀 호출

MISSED:
- 물고기 대이동 오류: 실시간으로 변하는 fishes 정보 참조
"""
from copy import deepcopy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def fish_moves(p_MAP, p_fishes, sx, sy):
    for idx in range(1, 17):  # 1 ~ 16 번 차례대로 이동
        if idx not in p_fishes:
            continue
        cx, cy, d = p_fishes[idx]
        for k in range(8):
            nd = (d + k) % 8  # 다음 방향
            nx, ny = cx + dx[nd], cy + dy[nd]  # 다음 위치
            if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != (sx, sy) and 0 <= p_MAP[nx][ny] <= 16:
                if p_MAP[nx][ny] == 0:  # 물고기 없는 칸
                    p_MAP[nx][ny] = idx
                    p_MAP[cx][cy] = 0
                    p_fishes[idx] = [nx, ny, nd]
                else:
                    target = p_MAP[nx][ny]
                    p_MAP[cx][cy], p_MAP[nx][ny] = p_MAP[nx][ny], p_MAP[cx][cy]  # swap
                    p_fishes[idx] = [nx, ny, nd]
                    p_fishes[target] = [cx, cy, p_fishes[target][2]]
                break


def dfs(p_MAP, p_fishes, sx, sy, total):
    # 0. 전처리 : MAP, fish 복사본 만들기 -> backtracking 용 임시 data
    c_MAP = [m[:] for m in p_MAP]
    c_fishes = deepcopy(p_fishes)

    # 1. 잡아 먹고
    to_eat = c_MAP[sx][sy]  # 잡아 먹힐 물고기 인덱스
    sx, sy, sd = c_fishes[to_eat]

    total += to_eat
    global res
    if total > res:
        res = total

    # 맵 정보, 물고기 정보 갱신
    c_MAP[sx][sy] = 0  # 물고기 없음
    del c_fishes[to_eat]

    # 2. 물고기 대이동
    fish_moves(c_MAP, c_fishes, sx, sy)

    # 3. 상어 이동
    for step in range(1, 4):
        nx, ny = sx + dx[sd] * step, sy + dy[sd] * step
        if 0 <= nx < 4 and 0 <= ny < 4 and c_MAP[nx][ny] > 0:  # 범위 밖을 벗어나지 않고 물고기 있는 경우
            dfs(c_MAP, c_fishes, nx, ny, total)


res = 0  # 최종 결과값
fishes = dict()  # 물고기 정보 저장 -> 번호 : [x, y, d]
MAP = [[0] * 4 for _ in range(4)]  # 물고기 위치 기록
for i in range(4):
    fish = list(map(int, input().split()))
    fishes[fish[0]] = [i, 0, fish[1] - 1]
    fishes[fish[2]] = [i, 1, fish[3] - 1]
    fishes[fish[4]] = [i, 2, fish[5] - 1]
    fishes[fish[6]] = [i, 3, fish[7] - 1]
    MAP[i][0], MAP[i][1], MAP[i][2], MAP[i][3] = fish[0], fish[2], fish[4], fish[6]

# DFS Backtracking
dfs(MAP, fishes, 0, 0, 0)  # MAP, fish 정보, shark_x, shark_y, total

print(res)
