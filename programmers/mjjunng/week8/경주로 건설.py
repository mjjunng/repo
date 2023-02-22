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
