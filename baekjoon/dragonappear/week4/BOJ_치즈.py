# https://www.acmicpc.net/problem/2638
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

"""
sol1 - dfs(timeout)
1. 바깥 0에 전처리
2. 남아있는 1에 대해서 사라질 대상인지 체크
3. 치즈 지우기
4. 치즈가 사라질때까지 반복

sol2 - bfs
1. 0에 대해서 BFS 순회(0만 순회하기 위해 0만 큐에 삽입)
2. 0에서 1로 순회시 큐에 넣지않고 1에 방문횟수 추가
3. 0 방문 모두 끝나면 치즈 지우기 + 남은 치즈는 원복
4. 치즈가 사라질때까지 반복

time: O(NM) n,m=[1,100]
space: O(NM) n,m=[1,100]
"""

def bfs():
    q=deque([(0,0)])
    visited = [ [False] * M for _ in range(N)] # 방문 체크 변수
    visited[0][0]=True
    
    while q: # BFS
        row,col=q.popleft()
        for dr,dc in dr_dc:
            nr,nc = row+dr,col+dc
            if (0<=nr<N) and (0<=nc<M) and (not visited[nr][nc]):
                if graph[nr][nc]>=1: # 1이면 
                    graph[nr][nc] += 1 # 주변 0 개수 카운트
                else: # 0이면 
                    visited[nr][nc]=1 # 방문 표시
                    q.append((nr,nc))

# 초기화    
N,M=map(int,input().split()) # input
graph = [ list(map(int,input().strip().split())) for _ in range(N)] # 그래프
cheeze_count = sum( graph[i].count(1) for i in range(len(graph))) # 치즈 카운트
dr_dc=[(0,1),(0,-1),(-1,0),(1,0)] # 방향 변수
time = 0 # 시간 변수

# 치즈 지우기 작업
while True:
    if cheeze_count<=0: # 종료 조건: 남아있는 치즈가 없을 시
        break

    bfs() # 0에 대해서 BFS
    for row in range(N):
        for col in range(M):
            if graph[row][col] >= 3: graph[row][col],cheeze_count=0,cheeze_count-1 # 치즈 지우기
            elif graph[row][col] == 2: graph[row][col] = 1 # 치즈 원복
    time+=1
    
write(str(time))