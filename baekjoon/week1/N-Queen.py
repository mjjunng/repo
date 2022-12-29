def solution(n):
    answer = 0
    queen = [0 for _ in range(n)]

    def check(x):
        for i in range(x):
            if (queen[x] == queen[i]) or (abs(x - i) == abs(queen[x] - queen[i])):
                return False
        return True

    def dfs(p):
        nonlocal answer
        if p == n:
            answer += 1
            return

        for i in range(n):  # [p][모든 열]에 퀸 위치시킴
            queen[p] = i
            if check(p):  # 현재 놓은 퀸의 위치가 가능하다면
                dfs(p + 1)  # 다음 행에 퀸을 놓음

    dfs(0)
    return answer
