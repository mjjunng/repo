# https://www.acmicpc.net/problem/19236
from sys import stdin,stdout
from copy import deepcopy
input,write=stdin.readline,stdout.write

def dfs(sr,sc,tot,board):
    global mx
    
    tot += board[sr][sc][0]
    mx = max(mx, tot)
    board[sr][sc][0]=0

    # 물고기 위치 교체
    for fish in range(1, 17):
        fr,fc=-1,-1
        for r in range(4):
            for c in range(4):
                if board[r][c][0] == fish:
                    fr,fc=r,c
                    break
        
        if (fr == -1 and fc == -1): continue # 죽은 경우
        
        fd = board[fr][fc][1]
        for i in range(1,9):
            nd = (fd+i)%9
            if nd==0: nd=1
            
            nr,nc= (fr+dr_dc[nd][0]),(fc+dr_dc[nd][1])
            if not (0 <= nr < 4 and 0 <= nc < 4) or (nr == sr and nc == sc): # 인덱스 밖 or 상어
                continue 
            
            board[fr][fc][1]=nd
            board[fr][fc],board[nr][nc]=board[nr][nc],board[fr][fc]
            break
    
    # 상어 DFS
    sd = board[sr][sc][1]
    for i in range(1, 5):
        nr,nc=sr+dr_dc[sd][0]*i,sc+dr_dc[sd][1]*i
        if (0<=nr<4 and 0<=nc<4) and (board[nr][nc][0]>0):
            dfs(nr, nc, tot, deepcopy(board))


mx=float('-inf')
board=[[0]*4 for _ in range(4)]
dr_dc=[[0,0],[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
for i in range(4):
    tmp=list(map(int,input().strip().split()))
    for j in range(4):
        fish_num,fish_dir=tmp[2*j],tmp[2*j+1]
        board[i][j]=[fish_num,fish_dir]

dfs(0, 0, 0, board)

print(mx)