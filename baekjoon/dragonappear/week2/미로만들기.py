# https://www.acmicpc.net/problem/1347 미로만들기

import sys
input = sys.stdin.readline

"""풀이

시간복잡도: O(N)  N[1,50]=명령어 길이
공간복잡도: O(M^2)  M[1,50]=그래프 길이

문제 특징:
- 그래프의 m*n이 정해지지 않음
- 그래프가 없기 때문에 시작점도 없음
- 명령어를 통해 최종 그래프를 그릴수있도록 세팅하는 문제

<구현:실패>

1. 초기화
- 방향키 설정
- 정답 리스트 세팅 [[0]]

2. 명령어 진행
- 명령어진행될때마다 좌표 최신화 + 리스트 최신화하는 방식
-> 현재 방향 + 명령어마다 벽과 인덱스 밖을 리스트로 그려야 하므로 구현 어려움


<구현>

참고: https://velog.io/@wook2pp/%EB%B0%B1%EC%A4%80-1347-%EB%AF%B8%EB%A1%9C-%EB%A7%8C%EB%93%A4%EA%B8%B0

과정:
1. 초기화
- 방향키 설정
- 시작점 및 방향키 설정
- 좌표추적 리스트 세팅 [0,0]

2. 명령어 진행
- F 일경우 현재 좌표기준으로 다음좌표 초기화 + 좌표추적 리스트에 추가
- 방향 회전일 경우 방향키 변경

3. 좌표그리기 작업(좌표추적 리스트를 기준으로)
- 가로,세로 길이 구하기
- 그래프 출력

"""

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
    max_x = max_y = -sys.maxsize 
    min_x = min_y = sys.maxsize
    
    for pos in trace:
        min_x = min(min_x, pos[0])
        min_y = min(min_y, pos[1])
    
    for i in range(len(trace)):
        trace[i][0] , trace[i][1] = trace[i][0]-min_x , trace[i][1]- min_y
        max_x,max_y = max(max_x, trace[i][0]) , max(max_y, trace[i][1])
    
    result = [['#']*(max_y+1) for i in range(max_x+1)]
    for xy in trace:
        result[xy[0]][xy[1]] = '.'

    # 결과 출력
    for row in result:
        print(*row, sep='')