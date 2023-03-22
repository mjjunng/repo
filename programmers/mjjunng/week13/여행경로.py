# sol1) brute-force

import copy 

def solution(tickets):
    answer = []
    start = 'ICN'
    visited = [0 for _ in range(len(tickets))]
    
    def dfs(lev, start, path):
        if lev == len(tickets):
            answer.append(path)
            return
        
        for i in range(len(tickets)):
            if (tickets[i][0] == start) and (visited[i] == 0):
                visited[i] = 1
                p = copy.deepcopy(path)
                p.append(tickets[i][1])
                dfs(lev+1, tickets[i][1], p)
                visited[i] = 0
        
    dfs(0, start, [start])
    answer.sort()
    
    return answer[0]
  
# sol2) dfs + stack
from collections import defaultdict

def solution(tickets):
    start = 'ICN'
    path = []   # 최종 경로 저장
    stack = []  # 출발지 저장 
    board = defaultdict(list)
    
    # {출발지: [도착지]} 
    for a, b in tickets:
        board[a].append(b)
    
    # 도착지 내림차순 정렬 -> 알파벳 순서가 앞서는 경로로 먼저 탐색하기 위해  
    for k in board:
        board[k].sort(reverse=True)
    
    stack.append(start)
    
    while stack:
        top = stack[-1]
        
        if top not in board or len(board[top]) == 0:    # 더이상 탐색할 수 없을 때 
            path.append(stack.pop())
        else:
            stack.append(board[top].pop())  # 도착지(다음 출발지)를 stack에 append
            
    
    return path[::-1]
