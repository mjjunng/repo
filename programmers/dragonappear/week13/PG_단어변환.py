# https://school.programmers.co.kr/learn/courses/30/lessons/43163
def solution(begin, target, words):

    def check(a, b):
        cnt = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                cnt += 1
            if cnt >= 2:
                return False
        return True

    def dfs(st, cnt):
        nonlocal answer
        if st == target:
            if answer > cnt:
                answer = cnt
            return

        for i in range(N):
            if vis[i] or not check(st, words[i]):
                continue

            vis[i] = True
            dfs(words[i], cnt+1)
            vis[i] = False

    N = len(words)
    vis = [False] * N
    answer = float('inf')
    dfs(begin, 0)
    return answer if answer != float('inf') else 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
