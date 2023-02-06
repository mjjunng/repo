# https://www.acmicpc.net/problem/14499
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N,M,X,Y,K=map(int,input().split())
board=[[0] for _ in range(N)]
for i in range(N):
    board[i]=list(map(int,input().strip().split()))

r,c=X,Y    
dice=[0]*7
#   위=1,동=3
#      [2]
#   [4][1][3]
#      [5]
#      [6]

for cmd in list(map(int,input().split())):
    if cmd==1: # 동
        if not(0<=c+1<M): continue
        c=c+1
        dice[1],dice[6],dice[3],dice[4]=dice[4],dice[3],dice[1],dice[6]
        
    elif cmd==2: # 서
        if not(0<=c-1<M): continue
        c=c-1
        dice[1],dice[6],dice[3],dice[4]=dice[3],dice[4],dice[6],dice[1]
        
    elif cmd==3: # 북
        if not(0<=r-1<N): continue
        r=r-1
        dice[1],dice[6],dice[2],dice[5]=dice[5],dice[2],dice[1],dice[6]
        
    elif cmd==4: # 남 
        if not(0<=r+1<N): continue
        r=r+1
        dice[1],dice[6],dice[2],dice[5]=dice[2],dice[5],dice[6],dice[1]
    
    if board[r][c]==0: board[r][c]=dice[6]
    else: dice[6],board[r][c]=board[r][c],0
    
    print(dice[1])    