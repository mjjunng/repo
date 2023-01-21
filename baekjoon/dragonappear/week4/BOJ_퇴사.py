# https://www.acmicpc.net/problem/14501
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

"""
DP
중복하위문제+최적부분구조

time: O(N) n=[1,15]
space: O(1)
"""

N=int(input())
schedule = [(0,0)]+[ tuple(map(int,input().strip().split())) for _ in range(N) ]
dp = [ 0 ] * (1_001)

for i in range(N,-1,-1): # O(N)
    time = i + schedule[i][0]
    if(time>N+1):
        dp[i]=dp[i+1]
    else:
        dp[i]=max(dp[i+1],dp[time]+schedule[i][1])
    
write(str(dp[1])+"\n")