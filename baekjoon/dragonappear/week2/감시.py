# https://www.acmicpc.net/problem/15683 감시
import sys
from typing import List
input = sys.stdin.readline

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
        # 그래프 순회 및 체크
        process(col, row, direction, copy_graph)
        # 현재 그래프에서 dfs
        dfs(copy_graph, level + 1)
        # 그래프 리셋
        copy_graph = [ element[::] for element in graph]

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

    dfs(graph, 0)
    print(mn)