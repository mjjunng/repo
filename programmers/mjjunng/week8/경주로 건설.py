''' sol1) dfs + dp 
          dy, dx 방향 순서에 따라 정답 달라짐?? 
'''

answer = float('inf')

def solution(board):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    n = len(board)
    dp = [[float('inf') for _ in range(n)] for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    
    def dfs(y, x, cnt_straight, cnt_corner, d):
        global answer
        cost = cnt_straight * 100 + cnt_corner * 500
        
        if cost > answer:   
            return
        
        if dp[y][x] < cost:
            return
        else:
            dp[y][x] = cost
        
        if y == n-1 and x == n-1:
            if cost < answer:
                answer = cost
            return
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if (0 <= ny < n) and (0 <= nx < n):
                if board[ny][nx] == 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    if d == i or d == -1:    
                        dfs(ny, nx, cnt_straight+1, cnt_corner, i)
                    else:
                        dfs(ny, nx, cnt_straight+1, cnt_corner+1, i)
                    visited[ny][nx] = 0
                    
    visited[0][0] = 1
    dfs(0, 0, 0, 0, -1)
    
    return answer


# sol2) bfs -- 최단 거리 문제는 bfs로 풀기!!
from collections import deque

def solution(board):
    answer = float('inf')
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    n = len(board)
    dp = [[float('inf') for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append([0, 0, -1, 0])
    dp[0][0] = 0
    
    while q:
        y, x, d, cost = q.popleft()
        
        # 탐색할 비용이 이미 answer보다 크다면, 더이상 탐색할 필요 없으므로, cut-edge
        if cost > answer:
            continue
        
        # 이미 탐색한 비용이 탐색할 비용보다 작다면, 더이상 탐색할 필요 없으므로, cut-edge
        if dp[y][x] < cost:
            continue
            
        if y == n-1 and x == n-1:
            if cost < answer:
                answer = cost
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if (0 <= ny < n) and (0 <= nx < n):
                if board[ny][nx] == 0 and dp[ny][nx] > cost:
                    c = 0
                    if i == d or d == -1:
                        c = cost + 100
                    else:
                        c = cost + 600
                        
                    dp[ny][nx] = c
                    q.append([ny, nx, i, c])
    
    return answer
