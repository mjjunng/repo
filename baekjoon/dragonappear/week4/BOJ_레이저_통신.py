# https://www.acmicpc.net/problem/6087
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write


"""
BFS를 활용한 최단거리 문제
거리를 묻는거같지만, 종료점까지 최소 거울을 사용하여 도달하면 되는 문제
각 정점에 최소 거울로 갈 수 있는 그래프를 그리기

time:O(W^2+H^2) W,H=[1,10^2]
space:O(WH)
"""

# 초기화
w,h = map(int, input().split())
graph = [input() for _ in range(h)]

# C 좌표 저장
c = []
for i in range(h):
    for j in range(w):
        if graph[i][j] == "C":
            c.append((i, j))

# 초기화
dx_dy=[(0,1),(0,-1),(-1,0),(1,0)] # 방향
(start_x, start_y), (end_x, end_y) = c # 시작,종료점 
check = [ [float("inf")] * w for _ in range(h)] # 체크표시

# BFS
queue = deque([(start_x, start_y)])
check[start_x][start_y] = 0
while queue: # O(WH)
    cur_x, cur_y = queue.popleft()

    # 종료점
    if cur_x == end_x and cur_y == end_y:
        write(str(check[cur_x][cur_y] - 1))
        exit()

    for dx,dy in dx_dy: #O(W+H)
        next_x, next_y = cur_x + dx, cur_y + dy
        while True:
            
            # 범위 인덱스 , 벽 , 이미 방문한 정점이면 break
            if not (0 <= next_x < h and 0 <= next_y < w) or graph[next_x][next_y] == "*" or check[next_x][next_y] < check[cur_x][cur_y] + 1:
                break
            
            # 큐에 다음에 순회할 좌표 저장
            queue.append((next_x, next_y))
            check[next_x][next_y] = check[cur_x][cur_y] + 1
            next_x = next_x + dx
            next_y = next_y + dy