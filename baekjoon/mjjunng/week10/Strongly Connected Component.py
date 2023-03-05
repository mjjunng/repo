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

2. Tarjan 알고리즘
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

        
import sys
sys.setrecursionlimit(10**6)

'''
2. Tarjan 알고리즘
모든 정점에 대해 dfs 수행해서 scc 찾는 방식 
- 인접 노드에 방문하며, 자기 자신을 스택에 넣고 재귀적으로 dfs 수행
- 인접 노드에 방문했을 때 아직 dfs 중인 경우, 자신의 부모값과 인접 노드의 부모값 중 작은 값으로 부모 값 갱신
- 부모 값과 자신의 노드 값이 같으면, 스택에서 자신이 나올 때 까지 뽑는다. 
'''
# sol3) Tarjan 알고리즘

stack = []
id = 1

def dfs(node):
    global id
    d[node] = id    # 노드에 고유 번호 할당 (부모 값 설정)
    id += 1
    stack.append(node)

    parent = d[node]    # 노드의 부모를 고유 번호로 초기화

    for i in board[node]:
        # dfs를 돌지 않은 노드일 때는 dfs 돌고, dfs 돌면서 해당 노드의 부모의 값이 더 작은 경우
        # 현재 노드의 부모값을 갱신한다.
        if d[i] == 0:
            parent = min(parent, dfs(i))

        # 인접 노드가 dfs 처리 중(stack에 존재)이라면, 해당 노드의 부모 값과
        # 자신의 부모값 중 작은 값으로 현재 노드의 부모 값을 갱신한다.
        elif finished[i] == 0:
            parent = min(parent, d[i])

    # 부모 노드가 자신인 경우
    if parent == d[node]:
        tmp = []
        while True:
            t = stack.pop()
            tmp.append(t)
            finished[t] = 1

            if t == node:
                break
        tmp.sort()
        scc.append(tmp)

    return parent

if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    v, e = map(int, input().split())
    board = [[] for _ in range(v+1)]
    finished = [0 for i in range(v+1)]  # scc에 이미 들어있는 노드인지 확인
    d = [0 for i in range(v+1)]   # 노드의 고유 번호 할당
    scc = []

    for _ in range(e):
        a, b = map(int, input().split())
        board[a].append(b)

    for i in range(1, v+1):
        if d[i] == 0:
            dfs(i)

    scc.sort()
    print(len(scc))

    for i in scc:
        print(*i, -1)

