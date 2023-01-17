"""
BFS + DP
- (x좌표, y좌표, 방향 정보, 거울 개수)을 저장한 큐로
- 네가지 방향에 대해 탐색할 때, 현재와 다른 방향일 때 거울 추가
    -> 해당 위치까지 최소 거울 개수를 저장한 DP값과 비교해서 방문 큐에 추가 (작거나 같으면 갱신, 큐 추가)
"""
import sys
from collections import deque
input = sys.stdin.readline

w, h = map(int, input().split())
MAP = [input() for _ in range(h)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

pos = []  # 'C' 위치 정보
for i in range(h):
    for j in range(w):
        if MAP[i][j] == 'C':
            pos.append((i, j))

# pos0 -> pos1 BFS 탐색하며 최소 거울 개수 업데이트
dp = [[int(1e9)] * w for _ in range(h)]  # 최소 거울 개수 업데이트 용도 && 방문 표시
sx, sy = pos[0][0], pos[0][1]  # 시작점
queue = deque([(sx, sy, 0, 0), (sx, sy, 1, 0), (sx, sy, 2, 0), (sx, sy, 3, 0)])  # (x좌표, y좌표, 방향 정보, 거울 개수)
tx, ty = pos[1][0], pos[1][1]  # 목표점
while queue:
    cx, cy, cDir, cCnt = queue.popleft()
    for dDir, d in enumerate(dirs):
        dx, dy = d
        if 0 <= cx + dx < h and 0 <= cy + dy < w and MAP[cx + dx][cy + dy] in {'.', 'C'}:
            nxtCnt = cCnt if dDir == cDir else cCnt + 1  # 방향 전환 여부에 따른 거울 개수
            if nxtCnt <= dp[cx + dx][cy + dy]:  # 거울 개수가 기존 DP값 보다 작거나 같으면 큐 추가
                dp[cx + dx][cy + dy] = nxtCnt
                queue.append((cx + dx, cy + dy, dDir, nxtCnt))

print(dp[tx][ty])