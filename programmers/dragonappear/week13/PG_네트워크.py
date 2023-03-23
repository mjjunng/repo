# https://school.programmers.co.kr/learn/courses/30/lessons/43162
def solution(n, computers):

    def dfs(i):
        for j in range(n):
            if vis[j] or computers[i][j] == 0:
                continue
            vis[j] = True
            dfs(j)

    vis = [False]*n
    ans = 0
    for i in range(n):
        if vis[i]:
            continue
        vis[i] = True
        dfs(i)
        ans += 1
    return ans


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
