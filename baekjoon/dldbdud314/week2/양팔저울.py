'''
DFS + DP

DFS -> 구슬이 왼쪽에 고정 되어 있다고 했을 때,
- 해당 추를 왼쪽 저울에 놓는다
- 해당 추를 놓지 않는다
- 해당 추를 오른쪽 저울에 놓는다

cnt개의 추를 놨을 떄, weight 그램을 만들 수 있음 -> DP[cnt][weight] = True
'''

n = int(input())
weights = list(map(int, input().split()))
m = int(input())
marbles = list(map(int, input().split()))


# n개로 만들 수 있는 무게 반영 -> DP
def dfs(cnt, weight):
    #종료 조건
    if dp[cnt][weight] or weight > 40000:
        return

    dp[cnt][weight] = True

    if cnt < n:
        dfs(cnt + 1, weight + weights[cnt])
        dfs(cnt + 1, weight)
        dfs(cnt + 1, abs(weight - weights[cnt]))


dp = [[False] * 40001 for _ in range(31)]  # n개의 추로, k 그램을 만들 수 있는가?: DP[n][k]
dfs(0, 0)
for marble in marbles:
    if dp[n][marble]:
        print('Y', end=' ')
    else:
        print('N', end=' ')