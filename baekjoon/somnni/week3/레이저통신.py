from collections import deque
# 왼쪽 오른쪽 이동
dx = [0,0,1,-1]
# 위 아래 이동
dy = [1,-1,0,0]
w, h = map(int,input().split())
a = [input() for _ in range(h)]
start = [0,0]
end = [0,0]
cnt = 0
# 맨 처음 찾은 C 지점을 시작, 그 뒤의 지점은 destination 으로 설정
for i in range(h):
    for j in range(w):
        if a[i][j] == 'C':
            if cnt == 0:
                start[0] = i
                start[1] = j
                cnt+= 1
            else:
                end[0] = i
                end[1] = j
# 방문한 지점을 기록
d = [[-1]*w for _ in range(h)]
# 위, 아래, 왼쪽, 오른쪽을 봐줘야 하는 지점을 넣음
# 한 지점에 도착할 때마다 q 에 그 지점의 위치를 넣는다
q = deque()
# 시작점을 기록
d[start[0]][start[1]] = 0
q.append((start[0],start[1]))
# q 가 empty 이면, 모든 지점 탐색을 의미
while q:
    # 제일 먼저 넣은 지점을 q 에서 빼낸다
    x,y = q.popleft()
    for k in range(4):
        # 방향을 위, 아래, 왼쪽, 오른쪽으로 갈지 정한다
        i = x+dx[k]
        j = y+dy[k]
        # 인덱스 범위 밖이거나 벽이 나올 때까지 같은 방향으로 계속 이동
        while 0 <= i < h and 0 <= j < w:
            if a[i][j] == '*':
                break
            # 이동할 때마다 이동한 지점을 전에 방문 안 했다면 이 지점 도착하기 전의 레이저 수 + 1 해줌
            if d[i][j] == -1:
                d[i][j] = d[x][y] + 1
                q.append((i,j))
            i += dx[k]
            j += dy[k]
# d에 -1로 남은 지점들은 다 벽이고 각 지점마다 시작점으로부터 최소 레이저 수 알 수 있음
print(d[end[0]][end[1]]-1)