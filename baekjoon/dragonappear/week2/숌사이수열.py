# https://www.acmicpc.net/problem/1469 숌사이수열

import sys
input = sys.stdin.readline


"""풀이

문제특징:
- 배열에 숫자 a의 첫번째 인덱스 x에 값을 넣으면, 숫자 a의 두번째 인덱스 y의 위치는 고정이 됨.

<DFS>

- 순열문제여서 DFS로 접근
- arr[index], arr[index + x[i] +1]를 같이 초기화하는 방식으로 진행
- 위치가 고정되어 있기 때문에, 삽입할 위치에 다른 값이 있으면 백트래킹
- 백트래킹 조건:
    - 인덱스 범위를 넘어섰는 경우
    - 이미 해당 인덱스에 방문 했는 경우
    - 배열에 값이 있는 경우

"""

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

    # 1. 초기화
    n = int(input())
    x =  list(map(int,input().split()))    
    visited = [False] * (2*n)
    result = [None] * (2*n)
    x.sort()

    # 2. 초기화,출력
    dfs(0)

    # 3. 출력
    print(-1)