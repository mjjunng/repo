'''
    첫 번째 풀이: dfs 
    - 시간 초과 실패 
'''

ans = set()
def dfs(lev, left, right):
    if lev == n:
        res = max(left, right) - min(left, right)
        ans.add(res)
        return

    dfs(lev+1, left+weights[lev], right)
    dfs(lev+1, left, right+weights[lev])
    dfs(lev+1, left, right)

if __name__ == "__main__":
    n = int(input())
    weights = list(map(int, input().split()))

    m = int(input())
    vals = list(map(int, input().split()))


    dfs(0, 0, 0)

    for val in vals:
        if val in ans:
            print("Y", end=' ')
        else:
            print("N", end=' ')


