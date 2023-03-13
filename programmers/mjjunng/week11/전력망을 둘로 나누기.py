from collections import deque

# 연결된 노드의 개수 리턴 
def bfs(n, board, k):
    visited = [0 for _ in range(k+1)]
    visited[n] = 1
    q = deque()
    q.append(n)
    cnt = 0
    
    while q:
        now = q.popleft()
        cnt += 1
        
        for i in board[now]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
                
    return cnt

def solution(n, wires):
    answer = float('inf')
    board = [[] for _ in range(n+1)]
    
    for a, b in wires:
        board[a].append(b)
        board[b].append(a)
    
    for a, b in wires:
        board[a].remove(b)  # 전선 끊기 
        board[b].remove(a)
        cnt = bfs(1, board, n)
        answer = min(abs(cnt - (n - cnt)), answer)
        board[a].append(b)  # 전선 복구 
        board[b].append(a)
    
    return answer
