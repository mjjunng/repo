'''
다익스트라 (min heap 활용)
'''
from heapq import heappush, heappop

INF = int(1e9)


def dijkstra(start, time, graph):
    queue = []
    heappush(queue, (0, start))  # (시간, 노드)
    time[start] = 0
    while queue:
        t, cur = heappop(queue)  # MIN NODE
        if time[cur] < t:
            continue
        # MIN NODE 거쳐 가는 경우 VS. 기존 값 -> time 테이블 갱신
        for b, c in graph[cur]:
            cost = t + c
            if cost < time[b]:
                time[b] = cost
                heappush(queue, (cost, b))


def solution(N, road, K):
    time = [INF] * (N + 1)  # 시간(=비용) 정보
    graph = [[] for _ in range(N + 1)]  # graph[a] = [(b, c), ...] -> a에서 b로 가는 시간 c
    for a, b, c in road:
        graph[a].append((b, c))  # 양방향 연결
        graph[b].append((a, c))

    dijkstra(1, time, graph)

    count = [k for k in time if k <= K]

    return len(count)
