'''
16929. Two Dots

** DFS로 사이클 존재하는지 판별
- 이전 노드와 현재 노드 정보를 같이 넘겨서 이전 노드 제외 다음 방향에 대해 방문 여부 체크
- 방문 했으며 길이가 4이상인 경우 TRUE
'''
import sys
sys.setrecursionlimit(10**5)

isCycle = False


# 직전 노드와 현재 노드 함께 넘겨줘서 왔던 방향으로 가지 않게끔 한다
def dfs_find_cycle(px, py, cx, cy, v):
    v.add((cx, cy))
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        # 이전 위치와 다른 위치 + 같은 색인 경우
        if 0 <= cx + dx < n and 0 <= cy + dy < m and (cx + dx, cy + dy) != (px, py) and MAP[cx + dx][cy + dy] == MAP[cx][cy]:
            if (cx + dx, cy + dy) not in v:
                dfs_find_cycle(cx, cy, cx + dx, cy + dy, v)
            elif (cx + dx, cy + dy) in v and len(v) >= 4:
                global isCycle
                isCycle = True
                return


n, m = map(int, input().split())
MAP = [input() for _ in range(n)]

visited = set()
for i in range(n):
    for j in range(m):
        if (i, j) not in visited:
            dfs_find_cycle(-1, -1, i, j, visited)  # 이전 위치, 현재 위치, 점 개수 함께

print("Yes") if isCycle else print("No")
