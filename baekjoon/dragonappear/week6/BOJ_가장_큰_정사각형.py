# https://www.acmicpc.net/problem/1915
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

N,M=map(int,input().split())
tmp=[list(map(int,input().strip())) for _ in range(N)]
board = [[0]*(M+2) for _ in range(N+2)] # 테이블: [i][j]를 포함하는 정사각형의 최대 변 길이
for i in range(1,N+1): # 패딩 처리
    for j in range(1,M+1):
        board[i][j]=tmp[i-1][j-1]
mx=0    
for i in range(1,N+1):
    for j in range(1,M+1):
        if board[i][j]==0: continue
        board[i][j]=min(board[i-1][j-1],board[i][j-1],board[i-1][j])+1 # 점화식
        mx=max(mx,board[i][j])

print(mx*mx)