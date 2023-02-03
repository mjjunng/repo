# https://www.acmicpc.net/problem/16954
from sys import stdin,stdout
from collections import deque
input,write=stdin.readline,stdout.write

def bfs():
    visit=[[False] * 8 for _ in range(8)]
    visit[7][0]=True
    q=deque([[7,0]])
    while q:
        r,c=q.popleft()
        for dr,dc in dr_dc:
            nr,nc=r+dr,c+dc
            if not(0<=nr<8) or not(0<=nc<8) or board[nr][nc]=='#': continue
            if nr==0: return 1
            if not visit[nr-1][nc] and board[nr-1][nc]!='#':
                visit[nr-1][nc]=True
                q.append([nr-1,nc])
    return 0
    
board= [list(input().strip()) for _ in range(8)]
dr_dc=[[0,1],[0,-1],[-1,0],[1,0],[1,-1],[1,1],[-1,-1],[-1,1],[0,0]]
print(bfs())