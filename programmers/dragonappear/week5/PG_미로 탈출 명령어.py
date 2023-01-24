# https://school.programmers.co.kr/learn/courses/30/lessons/150365
def solution(n, m, x, y, r, c, k):
    answer = ''
    dist = abs(x-r)+abs(y-c)
    k -= dist
    
    # 예외처리
    if k < 0 or k%2 != 0: return "impossible"
    
    # 초기화
    direction = {'d':0, 'l':0, 'r':0, 'u':0}
    if (x > r): direction['u'] += x-r
    else: direction['d'] += r-x
    
    if (y > c): direction['l'] += y-c
    else: direction['r'] += c-y
    
        
    answer += 'd'*direction['d']
    # 나머지 처리
    d = min(int(k/2), n-(x+direction['d']))
    answer += 'd'*d
    direction['u'] += d
    k -= 2*d
    
    answer += 'l'*direction['l']
    # 나머지 처리
    l = min(int(k/2), y-direction['l']-1)
    answer += 'l'*l
    direction['r'] += l
    k -= 2*l
    
    answer += 'rl'*int(k/2)
    answer += 'r'*direction['r']
    answer += 'u'*direction['u']
    
    return answer

print(solution(3,4,2,3,3,1,5))
print(solution(2,2,1,1,2,2,2))
print(solution(3,3,1,2,3,3,4))

"""
Idea
같은 칸의 중복 방문이 가능, 인덱스 범위 안에 있는 주변 모든 칸 방문가능
사전 순으로 가장 빠른 경로(d>l>r>u) 때문에, d나 l 방향으로 먼저 움직여야함
d,l,r,u 순으로 탐색하는 깊이 k의 DFS or BFS로 구현시 4^2500 이므로 시간초과날것

기본적으로 최대한 d나 l 방향으로 움직인 후에 도착점으로 향하는 것이 유리하기 때문에, 격자와 k 조건 내에서 가장 아래, 가장 왼쪽으로 이동한 뒤 도착점으로 향하게 한다.
- 즉, (n,1) 위치를 거친 후 도착점으로 향하면 된다. 
- 이때 도착점으로 가는 최단거리보다 d나 l방향으로 1번 더 움직이면 반대 방향으로도 1번 움직여야 도착점에 돌아올 수 있다.
- 이를 감안하며 (n,1)에 도달했는데도 경로의 길이가 k보다 짧다면, 'rl'이나 'ud' 쌍을 모자란만큼 추가해주면 된다. 
- 둘 중 'rl' 쌍이 사전 순으로 더 빠르므로 'rl'을 모자란 길이의 절반 개수만큼 채워주고 r,u 방향 순서로 움직여 도착점에 들어가면 된다.
시간복잡도 O(1)
"""