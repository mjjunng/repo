def answer(info, a, p, sheep, wolf, msg, visited):
    if sheep <= wolf:
        msg = ""
        return 0
    mx = 0
    for i in range(1, len(visited)):
        if not visited[i] and visited[p[i]]:
            visited[i] = True
            if info[i] == 0:
                cnt = 1 + answer(info, a, p, sheep + 1, wolf, msg + str(i), visited)
            else:
                cnt = answer(info, a, p, sheep, wolf + 1, msg + str(i), visited)
            if cnt > mx:
                mx = cnt
            visited[i] = False
    return mx


def solution(info, edges):
    a = [[] for _ in range(len(info))]
    p = [0] * len(info)
    # 인접리스트 생성한다
    for i in range(len(edges)):
        a[edges[i][0]].append(edges[i][1])
        p[edges[i][1]] = edges[i][0]
    visited = [False] * len(info)
    visited[0] = True
    return 1 + answer(info, a, p, 1, 0, "", visited)