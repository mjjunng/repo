# https://www.acmicpc.net/problem/1041
from sys import stdin,stdout
input,write=stdin.readline,stdout.write

"""
그려보면서 풀이
1.주사위는 마주보는 짝이 정해지는것 고려
2.작은수부터 더해주면 된다.
3.위치마다 더할수있는 개수가 정해짐

time:O(NlogN) N=[1,1_000_000]
space:O(N) N=[1,1_000_000]
"""

n=int(input())
dice=list(map(int,input().split()))
if n==1:
    dice.sort()
    write(str(sum([dice[i] for i in range(0,5)]))+"\n")
else:
    nums = [ min(dice[i],dice[5-i]) for i in range(0,3)] # (0,5) (1,4) (2,3)
    nums.sort()
    
    result = 0
    result += ((n-2)*(n-2) + 4*(n-1)*(n-2)) * nums[0] # 1면
    result += ( 4*(n-1) + 4*(n-2) ) * (nums[0]+nums[1]) # 2면
    result += (4 * (nums[0]+nums[1]+nums[2])) # 3면

    write(str(result)+"\n")