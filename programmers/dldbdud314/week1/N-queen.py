ans = 0


# (x, y) 위치에 놓을 수 있는가? -> 열과 대각선 확인
def is_promising(row, x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def n_queen(row, x, n):
    if x == n:
        global ans
        ans += 1
        return

    for y in range(n):
        row[x] = y  # (x, y) 위치에 말을 놓는다
        if is_promising(row, x):
            n_queen(row, x + 1, n)


def solution(n):
    row = [0] * n
    n_queen(row, 0, n)
    return ans
