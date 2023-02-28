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
            
            
# sol2)  
