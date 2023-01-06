# https://www.acmicpc.net/problem/15683 감시
import sys
from typing import List
input = sys.stdin.readline

"""풀이
<DFS>

왜: 
- cctv 타입마다 방향이 다르고, cctv 각각의 방향이 결과에 영향을 주기 때문에 각 cctv의 모든 방향에 대해서 탐색을 해야함.
- 브루트포스로 풀기에는 코드가 너무 김.
- 노드를 cctv로 설정한 후 dfs로 품.

노드: cctv
과정:

1. 초기화
- cctv 좌표,방향 저장
- cctv 타입별 방향 설정

2. dfs(저장된 cctv 좌표순으로 진행)

- 종료점
    - cctv 끝까지 도달한 경우 그래프 색칠이 완료되었으므로, 사각지대 최솟값 업데이트

- 해당 cctv 타입의 방향마다 진행
    - process: cctv 타입별로 정해진 방향으로 색칠
    - dfs: 다음 cctv로 진행
    - cctv 타입별로 정해진 방향으로 색칠한거 해제
"""


# dfs
def dfs(graph:List[List[str]],level:int)->None:

    global mn

    # 종료점 -> 모든 cctv 순회 완료했을때
    # 최솟값 업데이트
    if level == len(cctvs):
        zero_count = sum( graph[i].count("0") for i in range(len(graph)))
        mn = min(mn,zero_count)
        return

    copy_graph = [ element[::] for element in graph] # 그래프 복사
    col, row, type = cctvs[level] # 0,0,'1'

    for direction in directions[int(type)-1]:
        process(col, row, direction, copy_graph) # 그래프 순회 및 체크
        dfs(copy_graph, level + 1) # 현재 그래프에서 dfs
        copy_graph = [ element[::] for element in graph] # 그래프 리셋

# 그래프 순회 및 체크
def process(row:int, col:int, direction:List, graph:List[List[str]]):

    for element in direction:
        next_row, next_col = row, col
        
        # 벽을 만나거나 익덱스 벗어나기 전까지 진행
        while True:
            next_row += dx_dy[element][0]
            next_col += dx_dy[element][1]

            if 0 <= next_row < n and 0 <= next_col < m:
                # '6' 일때 -> break
                if graph[next_row][next_col] == '6':
                    break
                # '0' 일때 -> '#' 체크
                if graph[next_row][next_col] == '0':
                    graph[next_row][next_col] = '#'
            # 맵 외 위치
            else:
                break

if __name__ == "__main__":

    # input
    n,m = map(int, input().split())
    graph = [ list(input().split()) for _ in range(n)]
    mn = sys.maxsize
    
    # 1. 초기화
    # cctv 정보 저장
    cctvs = [] 
    for row in range(n):
        for col in range(m):
            if '1' <= graph[row][col] <= '5':
                # cctv 좌표 및 타입 저장
                cctvs.append((row, col, graph[row][col]))

    # 방향 세팅
    dx_dy=[(-1,0),(1,0),(0,1),(0,-1)] # 상하좌우
    directions = [ 
        [[0], [1], [2], [3]], # cctv 1
        [[0, 1], [2, 3]], # cctv 2
        [[0, 2], [0, 3], [1, 2], [1, 3]], # cctv 3
        [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], # cctv 4
        [[0, 1, 2, 3]] # cctv 5
    ]

    # 2. dfs
    dfs(graph, 0)

    # 3. 정답 출력
    print(mn)