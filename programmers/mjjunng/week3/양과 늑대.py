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
