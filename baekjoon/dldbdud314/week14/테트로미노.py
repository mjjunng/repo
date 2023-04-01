# 입력부
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

"""
** 1. Brute-force -> 조금,, 현타,,
"""


def get_sum(cx, cy):
    # 모든 경우의 수
    sets = [
        [(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(0, 0), (0, 1), (1, 0), (1, 1)],
        [(2, 0), (0, 1), (1, 1), (2, 1)], [(0, 0), (1, 0), (2, 0), (2, 1)], [(0, 0), (0, 1), (1, 0), (2, 0)], [(0, 0), (0, 1), (1, 1), (2, 1)],
        [(0, 0), (1, 0), (1, 1), (1, 2)], [(1, 0), (1, 1), (1, 2), (0, 2)], [(0, 0), (0, 1), (0, 2), (1, 2)], [(0, 0), (0, 1), (0, 2), (1, 0)],
        [(0, 0), (1, 0), (1, 1), (2, 1)], [(1, 0), (2, 0), (0, 1), (1, 1)], [(0, 0), (0, 1), (1, 1), (1, 2)], [(0, 1), (0, 2), (1, 0), (1, 1)],
        [(0, 0), (0, 1), (0, 2), (1, 1)], [(0, 0), (1, 0), (2, 0), (1, 1)], [(1, 0), (1, 1), (1, 2), (0, 1)], [(1, 0), (0, 1), (1, 1), (2, 1)]
    ]

    cur_max_sum = 0
    for dirs in sets:
        pos = 0
        cur_sum = 0
        for dx, dy in dirs:
            if 0 <= cx + dx < n and 0 <= cy + dy < m:
                cur_sum += board[cx + dx][cy + dy]
                pos += 1
        if pos == 4:
            cur_max_sum = max(cur_sum, cur_max_sum)
    return cur_max_sum


max_sum1 = 0
for i in range(n):
    for j in range(m):
        cur_max = get_sum(i, j)
        if max_sum1 < cur_max:
            max_sum1 = cur_max

print(max_sum1)

"""
다른 풀이

** 2. dfs
- 'ㅗ' 모양 제외하고 dfs - >모두 한붓그리기로 만들 수 있다는 특성 활용
- 'ㅗ' 모양은 따로 구현
"""


# 'ㅗ' 제외 다른 도형들 (한붓그리기 가능)
def dfs(cx, cy, cnt, cur_sum):
    if cnt == 4:
        global max_sum2
        max_sum2 = max(max_sum2, cur_sum)
        return

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0 <= cx + dx < n and 0 <= cy + dy < m and not visited[cx + dx][cy + dy]:
            visited[cx + dx][cy + dy] = True
            cnt += 1
            cur_sum += board[cx + dx][cy + dy]
            dfs(cx + dx, cy + dy, cnt, cur_sum)
            cur_sum -= board[cx + dx][cy + dy]
            cnt -= 1
            visited[cx + dx][cy + dy] = False


max_sum2 = 0
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        # 'ㅗ' 제외 dfs 수행
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False

        # 'ㅗ' 따로 처리
        for dirs in [[(0, 0), (0, 1), (0, 2), (1, 1)], [(0, 0), (1, 0), (2, 0), (1, 1)], [(1, 0), (1, 1), (1, 2), (0, 1)], [(1, 0), (0, 1), (1, 1), (2, 1)]]:
            tmp_sum, pos = 0, 0
            for di, dj in dirs:
                if 0 <= i + di < n and 0 <= j + dj < m:
                    tmp_sum += board[i + di][j + dj]
                    pos += 1
            if pos == 4:
                max_sum2 = max(tmp_sum, max_sum2)

print(max_sum2)
