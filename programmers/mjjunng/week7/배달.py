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


# sol 2) dijkstra
import heapq
'''
    다익스트라 알고리즘: 하나의 정점에서 다른 모든 정점까지의 최소 경로 구하는 알고리즘
    
    1. 현재 위치한 노드의 방문하지 않은 인접 노드의 거리값 최소값으로 갱신, 방문 표시 
    2. 방문하지 않은 인접 노드 중 거리값이 가장 작은 노드 선택 
    3. 반복
'''
def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    answer = 0
    dis = [float('inf') for _ in range(N+1)]    # dis[idx]: 1번부터 idx까지 최소 거리 
    hq = []
    
    for r in road:
        n1, n2, v = r
        graph[n1].append([n2, v])
        graph[n2].append([n1, v])
        
    heapq.heappush(hq, [0, 1])  # [가중치, 노드]
    dis[1] = 0

    while hq:
        v, n = heapq.heappop(hq)    # 가중치가 가장 작은 노드 pop

        for node, val in graph[n]:
            if dis[n] + val < dis[node]:
                dis[node] = dis[n] + val
                heapq.heappush(hq, [dis[n] + val, node])
                
                
    for i in range(1, N+1):
        if dis[i] <= K:
            answer += 1    
    
    return answer
