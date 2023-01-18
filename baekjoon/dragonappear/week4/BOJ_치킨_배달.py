# https://www.acmicpc.net/problem/15686
from sys import stdin,stdout
from itertools import combinations
input,write=stdin.readline,stdout.write

"""
도시의 치킨 거리가 최소가 되도록 도시에 있는 치킨집 중 최대 M개를 고른다
1초,512MB
0,1,2=빈칸,집,치킨
N=[2,50],M=[1,13]

브루트포스
1초이므로 조합 다돌면서 계산해도 충분
time: O(N*M*(13)C(M)) N=[1,50] M=[1,13]
space: O(N^2+(13)C(M)) N=[1,50] M=[1,13]
"""

# 초기화            
N,M=map(int,input().split())
graph = [ list(map(int,input().split())) for _ in range(N) ]
dr_dc=[(0,1),(0,-1),(1,0),(-1,0)]
mn = float('inf')

# 집,치킨집 위치 저장
franchise,house=[],[]
for row in range(N):
    for col in range(N):
        if graph[row][col]==1:
            house.append((row,col))
        elif graph[row][col]==2:
            franchise.append((row,col))


# 치킨집 중 M개 선택
for selected in combinations(franchise,M): # O((13)C(M))
    dist_sum=0
    for hr,hc in house: # 집 돌면서 O(N)
        dist=float('inf')
        for index in range(M): # O(M)
            dist=min(dist,abs(hr-selected[index][0])+abs(hc-selected[index][1])) # 치킨 거리 찾기
        dist_sum+=dist # 도시의 치킨 거리에 찾은 치킨 거리 더하기
        if dist_sum>mn: break
    
    mn = min(mn,dist_sum)

write(str(mn))