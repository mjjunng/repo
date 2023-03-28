from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    
    for i in range(n):
        q = deque()
        if visited[i] == 0:
            q.append(i)
            visited[i] = 1
            answer += 1

            while q:
                now = q.popleft()

                for i in range(len(computers[now])):
                    if i != now and computers[now][i] == 1:
                        if visited[i] == 0:
                            q.append(i)
                            visited[i] = 1
                
                
    return answer
