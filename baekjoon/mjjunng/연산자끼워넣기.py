def dfs(lev, res):
    global min_res, max_res, op

    if lev == n:
        if res < min_res:
            min_res = res
        if res > max_res:
            max_res = res
        return

    for i in range(4):
        if op[i] > 0:
            if i == 0:
                op[i] -= 1
                dfs(lev+1, res+nums[lev])
                op[i] += 1
            elif i == 1:
                op[i] -= 1
                dfs(lev+1, res-nums[lev])
                op[i] += 1
            elif i == 2:
                op[i] -= 1
                dfs(lev+1, res*nums[lev])
                op[i] += 1
            else:
                op[i] -= 1
                if res < 0:
                    dfs(lev+1, ((res*-1)//nums[lev])*-1)
                else:
                    dfs(lev+1, res//nums[lev])
                op[i] += 1

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    op = list(map(int, input().split()))
    min_res = float('inf')
    max_res = -1 * float('inf')
    dfs(1, nums[0])

    print(max_res)
    print(min_res)
