# https://www.acmicpc.net/problem/1347 미로만들기
# 참고: https://velog.io/@wook2pp/%EB%B0%B1%EC%A4%80-1347-%EB%AF%B8%EB%A1%9C-%EB%A7%8C%EB%93%A4%EA%B8%B0

import sys
from collections import deque as dq
input = sys.stdin.readline

if __name__ == "__main__":
    
    n = int(input())
    commands = list(input())

    # 초기화
    dx_dy = [(-1,0),(0,1),(1,0),(0,-1)]
    dir_index, cur_x, cur_y = 2,0,0
    trace = [[0,0]]

    # [0,0] 인덱스를 기준으로 추적 리스트에 기록
    for command in commands:
        if command == 'F':
            cur_x += dx_dy[dir_index][0]
            cur_y += dx_dy[dir_index][1]
            trace.append([cur_x,cur_y])
            continue
        if command == 'L':
            dir_index -= 1
        elif command == 'R':
            dir_index += 1
        dir_index = (dir_index+4) % 4
    
    # 결과 생성
    max_x,min_x = -sys.maxsize,sys.maxsize
    max_y,min_y = -sys.maxsize,sys.maxsize
    
    for pos in trace:
        min_x = min(min_x, pos[0])
        min_y = min(min_y, pos[1])
    
    for i in range(len(trace)):
        trace[i][0] -= min_x
        trace[i][1] -= min_y
        max_x = max(max_x, trace[i][0])
        max_y = max(max_y, trace[i][1])
    
    result = [['#']*(max_y+1) for i in range(max_x+1)]
    for xy in trace:
        result[xy[0]][xy[1]] = '.'

    # 결과 출력
    for row in result:
        print(*row, sep='')