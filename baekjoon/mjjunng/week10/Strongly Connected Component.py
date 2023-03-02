# sol1) dfs: 시간 초과 

import sys

sys.setrecursionlimit(10**6)

def dfs(start, visited, end):
    global flg
    if flg:
        return

    for i in board[start]:
        if i == end:
            flg = True
            return

        if visited[i] == 0 and flg == False:
            visited[i] = 1
            dfs(i, visited, end)


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    v, e = map(int, input().split())
    board = [[] for _ in range(v+1)]
    complete = [0 for _ in range(v+1)]
    cnt = 0
    result = []

    for _ in range(e):
        a, b = map(int, input().split())
        board[a].append(b)

    for i in range(1, v+1):
        if complete[i] == 0:
            cnt += 1
            visited = [0 for _ in range(v+1)]
            visited[i] = 1
            flg = False
            dfs(i, visited, i)
            if flg:
                tmp = []
                for k in range(1, v+1):
                    if visited[k] == 1:
                        complete[k] = 1
                        tmp.append(k)
                result.append(tmp)

            else:
                result.append(i)

    print(cnt)
    for k in result:
        if str(type(k)) == "<class 'list'>":
            for i in k:
                print(i, end=' ')
            print(-1)
        else:
            print(k, -1)
            
            
import sys
sys.setrecursionlimit(10**6)

'''
Strongly Connected Component 문제를 푸는 방법
1. Kosaraju 알고리즘
- 정방향 그래프로 모든 노드에 대해서 dfs 수행 
- dfs 종료되는 순서대로 stack에 append
- stack에서 pop하면서, 역방향 dfs 수행 
- 역방향 dfs 하면서 노드 stack에 append -> scc 

'''
# sol2) Kosaraju 알고리즘
stack = []

# 정방향 dfs
def dfs(node, visited):
    for i in board[node]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, visited)

    stack.append(node)

# 역방향 dfs
def reversed_dfs(node, visited):
    tmp.append(node)
    for i in reversed_board[node]:
        if visited[i] == 0:
            visited[i] = 1
            reversed_dfs(i, visited)


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    v, e = map(int, input().split())
    board = [[] for _ in range(v+1)]
    reversed_board = [[] for _ in range(v+1)]
    visited = [0 for _ in range(v+1)]
    scc = []

    for _ in range(e):
        a, b = map(int, input().split())
        board[a].append(b)
        reversed_board[b].append(a)

    for i in range(1, v+1):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, visited)

    visited = [0 for _ in range(v + 1)]

    while stack:
        tmp = []
        now = stack.pop()
        if visited[now] == 0:
            visited[now] = 1
            reversed_dfs(now, visited)
            scc.append(sorted(tmp))

    print(len(scc))
    scc.sort()

    for i in scc:
        print(*i, -1)

