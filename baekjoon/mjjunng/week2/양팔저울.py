'''
    첫 번째 풀이: dfs 
    - O(3^n)으로 시간 초과 실패 
'''
ans = set()

def dfs(lev, left, right):
    if lev == n:
        res = max(left, right) - min(left, right)
        ans.add(res)
        return

    dfs(lev + 1, left + weights[lev], right)
    dfs(lev + 1, left, right + weights[lev])
    dfs(lev + 1, left, right)


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

'''
    두 번째 풀이: dfs + cut edge
    - cut edge: 두 무게의 차와 다음에 올릴 추의 무게가 이전과 같다면, 다음 가지로 뻗지 않아도 된다. 
    
'''
ans = set()

def dfs(lev, left, right):
    if lev == n:
        res = abs(left-right)
        ans.add(res)
        return

    if check[lev][abs(left-right)] == 1:
        return

    check[lev][abs(left - right)] = 1
    dfs(lev + 1, left + weights[lev], right)
    dfs(lev + 1, left, right + weights[lev])
    dfs(lev + 1, left, right)


if __name__ == "__main__":
    n = int(input())
    weights = list(map(int, input().split()))

    m = int(input())
    vals = list(map(int, input().split()))

    check =[[0 for _ in range(40001)] for _ in range(n)]    # check[i][j]: i: 다음에 올릴 추의 무게, j: 왼쪽과 오른쪽 무게의 차
    dfs(0, 0, 0)

    for val in vals:
        if val in ans:
            print("Y", end=' ')
        else:
            print("N", end=' ')
