from collections import deque

# bfs 

# 외부 공기 -1로 초기화
def initOutSide():
    dq = deque()
    visited_out = [[0 for _ in range(m)] for _ in range(n)]
    dq.append((0, 0))   # 0, 0부터 탐색 시작
    visited_out[0][0] = 1
    board[0][0] = -1

    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny < n) and (0 <= nx < m):
                if board[ny][nx] != 1:
                    if visited_out[ny][nx] == 0:
                        board[ny][nx] = -1
                        visited_out[ny][nx] = 1
                        dq.append((ny, nx))


# 치즈 모두 녹았는지 확인 
def isAllMelt():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                return False
    return True

if __name__ == "__main__":
    answer = 0
    n, m = map(int, input().split())
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]

    board = []

    for i in range(n):
        l = list(map(int, input().split()))
        board.append(l)
  
    # 치즈가 모두 녹을 때까지 반복 
    while not isAllMelt():
        initOutSide()
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1:
                    cnt = 0  # 외부 공기와 맞닿은 변의 개수
                    for k in range(4):
                        ny = i + dy[k]
                        nx = j + dx[k]

                        if (0 <= ny < n) and (0 <= nx < m):
                            if board[ny][nx] == -1:
                                cnt += 1
                    if 2 <= cnt:  # 외부 공기와 2변이 맞닿아 있다면 녹음 
                        board[i][j] = 0

        answer += 1

    print(answer)
