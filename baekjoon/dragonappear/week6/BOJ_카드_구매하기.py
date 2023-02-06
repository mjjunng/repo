# https://www.acmicpc.net/problem/11052
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

# N개 카드를 갖기 위해 지불해야 하는 금액의 최댓값
N=int(input())
A=[0]+list(map(int,input().split()))
d=[0]*(N+1) # d[i]=i개 카드를 갖기 위해 지불해야 하는 금액의 최댓값
d[1]=A[1]

for i in range(2,N+1):
    mx=float('-inf')
    for j in range(1,i):
        mx=max(mx,A[j]+d[i-j])
    d[i]=max(A[i],mx)
        
print(d[N])