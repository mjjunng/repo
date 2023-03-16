# https://school.programmers.co.kr/learn/courses/30/lessons/84512
def solution(word):

    def dfs(s):
        nonlocal cnt

        if len(s) == 5:
            return

        for w in ['A', 'E', 'I', 'O', 'U']:
            cnt += 1
            dic[s+w] = cnt
            dfs(s+w)

    cnt = 0
    dic = dict()
    dfs("")

    return dic[word]
