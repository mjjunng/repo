"""
1194. 달이 차오른다, 가자.

** BFS, bit masking 활용 - 풀이 참고
- 관건은 갔던 데를 또 갈 수 있다는 거 -> 무슨 기준으로 허용할 것인가..?
  -> 동일한 키 조합으로 방문한 적이 없는가? (비트마스크 활용)
"""
from collections import deque


def bfs():
    # 비트마스킹 -> 해당 키 조합으로 (x, y)에 방문한 적이 있는가 ?
    visited = [[[False] * (1 << 6) for _ in range(m)] for _ in range(n)]
    queue = deque([(sx, sy, 0, 0)])  # (현 위치 xy, 현 key 조합(누적), 거리 d)
    visited[sx][sy][0] = True

    while queue:
        cx, cy, ck, cd = queue.popleft()

        if maze[cx][cy] == '1':
            return cd  # 최단 경로 반환

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if 0 <= cx + dx < n and 0 <= cy + dy < m and not visited[cx + dx][cy + dy][ck] and maze[cx + dx][cy + dy] != '#':
                nk = ck  # 새로운 키 조합
                # key
                if 'a' <= maze[cx + dx][cy + dy] <= 'f':
                    nk = ck | 1 << (ord(maze[cx + dx][cy + dy]) - ord('a'))  # 키 조합 갱신
                # door
                elif 'A' <= maze[cx + dx][cy + dy] <= 'F':
                    # 열 수 없으면 PASS
                    if not (ck & 1 << (ord(maze[cx + dx][cy + dy]) - ord('A'))):
                        continue
                visited[cx + dx][cy + dy][nk] = True
                queue.append((cx + dx, cy + dy, nk, cd + 1))

    return -1  # 탈출 불가


n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(input())

# 시작점 찾아서 빈 공간으로 만들고, bfs 시작
sx, sy = None, None
for i in range(n):
    maze[i] = list(maze[i])
    for j in range(m):
        if maze[i][j] == '0':
            sx, sy = i, j
            maze[i][j] = '.'  # 빈 공간으로 처리
            break

print(bfs())
