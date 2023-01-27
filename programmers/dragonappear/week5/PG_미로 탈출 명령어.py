# https://school.programmers.co.kr/learn/courses/30/lessons/150365
def solution(n, m, x, y, r, c, k):
    
    # 예외처리
    # (x,y)->(r,c) 거리가 k 이상이거나, k 이하임에도 남은 거리가 홀수인 경우
    dist = abs(x-r)+abs(y-c)
    if dist>k or (k-dist)%2: return "impossible"
    
    # 1.목적지로 이동
    dcnt=lcnt=rcnt=ucnt=0
    
    if x<r: dcnt+=(r-x)
    else: ucnt+=(x-r)
    
    if y<c: rcnt+=(c-y)
    else: lcnt+=(y-c)
    
    # 2.왔다갔다 처리
    rest = k-dist
    
    dplus=min(n-max(x,r),rest//2)
    rest-=dplus*2
    
    lplus=min(min(y,c)-1,rest//2)
    rest-=lplus*2
    
    # 3.결과 도출
    return 'd'*(dcnt+dplus)+ 'l'*(lcnt+lplus)+ "rl"*(rest//2) + 'r'*(rcnt+lplus) + 'u'*(dplus+ucnt)

print(solution(3,4,2,3,3,1,5))
print(solution(2,2,1,1,2,2,2))
print(solution(3,3,1,2,3,3,4))
print(solution(3,3,1,2,3,3,5))

"""
Idea:
같은 칸의 중복 방문이 가능, 인덱스 범위 안에 있는 주변 모든 칸 방문가능
사전 순으로 가장 빠른 경로(d>l>r>u) 때문에, d나 l 방향으로 먼저 움직여야함
d,l,r,u 순으로 탐색하는 깊이 k의 DFS or BFS로 구현시 4^2500 이므로 시간초과날것

기본적으로 최대한 d나 l 방향으로 움직인 후에 도착점으로 향하는 것이 유리하기 때문에, 격자와 k 조건 내에서 가장 아래, 가장 왼쪽으로 이동한 뒤 도착점으로 향하게 한다.
즉, (r,1) 위치를 거친 후 도착점으로 향하면 된다. 
이를 감안하며 (r,1)에 도달했는데도 경로의 길이가 k보다 짧다면, 'rl'이나 'ud' 쌍을 모자란만큼 추가해주면 된다. 
둘 중 'rl' 쌍이 사전 순으로 더 빠르므로 'rl'을 모자란 길이의 절반 개수만큼 채워주고 r,u 방향 순서로 움직여 도착점에 들어가면 된다.
시간복잡도 O(1)
"""