"""
** 완전 탐색 DFS
"""
cnt, res = 0, 0


def dfs(cur, target):
    global cnt, res
    if len(cur) > 5:  # 종료 조건 : 길이 제한을 넘어갈 때
        return
    if cur == target:  # 동일한 단어면 종료
        res = cnt
        return

    cnt += 1  # 호출 횟수++
    for x in "AEIOU":
        dfs(cur + x, target)


def solution(word):
    dfs('', word)
    return res
