"""
백준 14499. 주사위 굴리기

<< 시뮬레이션(구현) >>
- 자료구조
    - dice : 주사위 전개도 인덱스에 맞게 숫자 저장
- 메인 로직: 바닥면에 따른 동서남북 이동, 숫자 변환
    - 굴리기: 전개도 재배치
    - 숫자 변환 로직
"""
import sys

input = sys.stdin.readline


def roll(dr, cur_d):  # 주사위 굴리기
    a, b, c, d, e, f = cur_d
    if dr == 1:  # 동쪽
        return [d, b, a, f, e, c]
    elif dr == 2:  # 서쪽
        return [c, b, f, a, e, d]
    elif dr == 3:  # 북쪽
        return [e, a, c, d, f, b]
    else:
        return [b, f, c, d, a, e]


dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 명령어에 따른 동서남북 이동 방향

n, m, x, y, k = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]

dice = [0] * 6
cmds = list(map(int, input().split()))  # 명령어 입력

for cmd in cmds:
    nx, ny = x + dirs[cmd - 1][0], y + dirs[cmd - 1][1]

    if 0 <= nx < n and 0 <= ny < m:  # 맵 밖을 벗어나지 않는 경우 이동
        x, y = nx, ny
        dice = roll(cmd, dice)  # 방향, 기존 전개도

        if MAP[x][y] == 0:
            MAP[x][y] = dice[-1]
        else:
            dice[-1] = MAP[x][y]
            MAP[x][y] = 0

        print(dice[0])
