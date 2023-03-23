# https://school.programmers.co.kr/learn/courses/30/lessons/43164
from collections import defaultdict


def solution(tickets):

    def dfs(u):
        while graph[u]:
            dfs(graph[u].pop())
        rst.append(u)

    graph = defaultdict(list)

    for u, v in sorted(tickets, reverse=True):
        graph[u].append(v)

    rst = []
    dfs("ICN")
    return rst[::-1]


print(solution([["ICN", "SFO"], ["ICN", "ATL"], [
      "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
