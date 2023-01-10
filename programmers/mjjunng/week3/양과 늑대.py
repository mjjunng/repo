'''
    첫 번째 풀이 방법: 완전 탐색
    0번째 노드에서 시작해서 방문하지 않은 모든 노드 탐색해서 양의 최대 마릿수 구함 -> 실패 & 시간초과 
'''

answer = 0

def solution(info, edges):
    visited = [0 for _ in range(len(info))]
    visited[0] = 1

    def search(node, sheep, wolf):
        global answer
        if sheep < wolf:
            return

        if sheep > answer:
            answer = sheep

        for i in range(len(info)):
            if visited[i] == 0:
                visited[i] = 1
                if info[i] == 0:
                    search(i, sheep +1, wolf)
                else:
                    search(i, sheep, wolf+1)
                visited[i] = 0
    search(0, 1, 0)
    return answer

'''
    두 번째 풀이 방법: dfs
    다음으로 갈 수 있는 노드 저장해서 탐색 
    - O(n * 2 ** n)
'''
answer = 0
def solution(info, edges):
    graph = [[] for _ in range(len(info))]  # graph[부모노드] = [자식 노드]
    for p, c in edges:
        graph[p].append(c)
    possible = []   # 다음 노드로 갈 수 있는 노드 저장 
    
    for node in graph[0]:
        possible.append(node)
    
    def dfs(pnode, sheep, wolf, possible):
        global answer
        # print(pnode, possible)
        if wolf >= sheep:
            return 
        answer = max(answer, sheep)

        for i in range(len(possible)):
            nxt = possible[:]
            cur = nxt.pop(i)
            for c in graph[cur]:
                nxt.append(c)
                
            if info[cur] == 0:
                dfs(cur, sheep+1, wolf, nxt)
            else:
                dfs(cur, sheep, wolf+1, nxt)

    dfs(0, 1, 0, possible)

    return answer
