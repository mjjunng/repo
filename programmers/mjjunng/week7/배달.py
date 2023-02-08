# sol 1) bfs

from collections import deque

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    answer = 0
    dis = [float('inf') for _ in range(N+1)]    # dis[idx]: 1번부터 idx까지 최소 거리 
    q = deque()
    
    for r in road:
        n1, n2, v = r
        graph[n1].append([n2, v])
        graph[n2].append([n1, v])
        
    q.append(1)
    dis[1] = 0

    while q:
        now = q.popleft()

        for node, val in graph[now]:
                if dis[node] > dis[now] + val:
                    dis[node] = dis[now] + val
                    q.append(node)
                
    for i in range(1, N+1):
        if dis[i] <= K:
            answer += 1    
    
    return answer
