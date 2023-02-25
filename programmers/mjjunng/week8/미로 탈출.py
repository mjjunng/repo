# bfs

from collections import deque

def solution(maps):
    answer_lever = 0
    answer_exit = 0
    l_y, l_x = -1, -1
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    q = deque()

    board = [[float('inf') for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    # 처음 시작 위치 q에 append
    flg = 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                q.append([i, j])
                board[i][j] = 0
                flg = 1
                break
        if flg == 1:
            break
    
    # 레버까지 최소 이동 시간 구하기 
    while q:
        y, x = q.popleft()
        
        if maps[y][x] == 'L':
            answer_lever += board[y][x]
            l_y, l_x = y, x
            break
            
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if (0 <= ny < len(maps)) and (0 <= nx < len(maps[0])):
                if maps[ny][nx] != 'X' and board[ny][nx] == float('inf'):
                    q.append([ny, nx])
                    board[ny][nx] = board[y][x] + 1
    
    # 레버부터 출구까지 최소 이동 시간 구하기 
    q = deque()
    board = [[float('inf') for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    if l_y >= 0 and l_x >= 0:
        q.append([l_y, l_x])
        board[l_y][l_x] = 0
    else:
        return -1
    
    while q:
        y, x = q.popleft()
        
        if maps[y][x] == 'E':
            answer_exit += board[y][x]
            break
            
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if (0 <= ny < len(maps)) and (0 <= nx < len(maps[0])):
                if maps[ny][nx] != 'X' and board[ny][nx] == float('inf'):
                    q.append([ny, nx])
                    board[ny][nx] = board[y][x] + 1
                    
    if answer_exit == 0:
        return -1
    
    return answer_exit + answer_lever
