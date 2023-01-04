# https://www.acmicpc.net/problem/1469 숌사이수열

import sys
input = sys.stdin.readline

# dfs
def dfs(level:int)->None:

    global result

    # 종료
    # 출력하고 종료
    if level == n*2:
        print(*result)
        sys.exit()
    
    # 이미 방문했으면 다음 레벨
    if level<n*2 and result[level] is not None:
        dfs(level+1)
        return

    for i in range(n):
        if ((visited[i]==False) 
                and (level + x[i] + 1 < 2*n) 
                and (result[level]==None) 
                and (result[level+x[i]+1]==None)):
            visited[i]=True
            result[level] = result[level+x[i]+1] = x[i]
            dfs(level+1)
            result[level] = result[level+x[i]+1] = None
            visited[i]=False

if __name__ == "__main__":
    n = int(input())
    x =  list(map(int,input().split()))    
    visited = [False] * (2*n)
    result = [None] * (2*n)
    x.sort()
    dfs(0)
    print(-1)