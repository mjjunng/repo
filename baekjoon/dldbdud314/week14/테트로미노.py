"""
14500. 테트로미노
** Brute-force
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


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

max_sum = 0
for i in range(n):
    for j in range(m):
        cur_max = get_sum(i, j)
        if max_sum < cur_max:
            max_sum = cur_max

print(max_sum)
