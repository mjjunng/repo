from collections import deque

def solution(maps):
    answer = 1
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1
    
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if (0 <= ny < n) and (0 <= nx < m):
                if maps[ny][nx] == 1:
                    if visited[ny][nx] == 0:
                        q.append([ny, nx])
                        visited[ny][nx] = visited[y][x] + 1
                        answer += 1
                        
    if visited[n-1][m-1] == 0:
        return -1
    else:
        return visited[n-1][m-1]
                    
