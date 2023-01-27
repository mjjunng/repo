# https://school.programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque

def solution(board):
    # 현재 좌표에서 이동가능한 좌표 리턴
    def move(pos1,pos2):
        ret=[]
        # 좌우상하 이동
        for dr,dc in dr_dc:
            if graph[pos1[0]+dr][pos1[1]+dc]==0 and graph[pos2[0]+dr][pos2[1]+dc]==0:
                ret.append({(pos1[0]+dr,pos1[1]+dc),(pos2[0]+dr,pos2[1]+dc)})
        
        # 가로에서 회전
        if pos1[0]==pos2[0]:
            for r in rotate:
                if graph[pos1[0]+r][pos1[1]]==0 and graph[pos2[0]+r][pos2[1]]==0: # 회전할 수 있는지 체크
                    ret.append({(pos1[0]+r,pos1[1]),(pos1[0],pos1[1])})
                    ret.append({(pos2[0]+r,pos2[1]),(pos2[0],pos2[1])})
        # 세로에서 회전
        elif pos1[1]==pos2[1]:
            for r in rotate:
                if graph[pos1[0]][pos1[1]+r]==0 and graph[pos2[0]][pos2[1]+r]==0: # 회전할 수 있는지 체크
                    ret.append({(pos1[0],pos1[1]),(pos1[0],pos1[1]+r)})
                    ret.append({(pos2[0],pos2[1]),(pos2[0],pos2[1]+r)})
            
        return ret
    
    N=len(board)
    dr_dc=[(1,0), (0,1), (-1,0), (0,-1)]
    rotate=[1,-1]
    
    graph=[[1]*(N+2) for _ in range(N+2)]
    for i in range(N):
        for j in range(N):
            graph[i+1][j+1] = board[i][j]
    
    q = deque([[(1,1),(1,2),0]])
    visit = [{(1,1),(1,2)}]
    
    while q:
        pos1,pos2,dist=q.popleft()
        dist+=1
        for rst in move(pos1,pos2):
            if (N,N) in rst:
                return dist
            if rst not in visit:
                q.append(list(rst)+[dist])
                visit.append(rst)
                
print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
