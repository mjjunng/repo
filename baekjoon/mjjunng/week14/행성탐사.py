import sys

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    input = sys.stdin.readline
    n, m = map(int, input().split())
    k = int(input())
    board = []
    dp = [[[0, 0, 0] for _ in range(m+1)] for _ in range(n+1)]

    for _ in range(n):
        board.append(list(input()))

    for i in range(n):
        for j in range(m):
            for r in range(3):
                dp[i+1][j+1][r] = dp[i+1][j][r] + dp[i][j+1][r] - dp[i][j][r]

            if board[i][j] == 'J':
                dp[i+1][j+1][0] += 1
            elif board[i][j] == 'O':
                dp[i+1][j+1][1] += 1
            else:
                dp[i+1][j+1][2] += 1

    for _ in range(k):
        a, b, c, d = map(int, input().split())
        answer = [0, 0, 0]
        for i in range(3):
            answer[i] = dp[c][d][i] - dp[a-1][d][i] - dp[c][b-1][i] + dp[a-1][b-1][i]
        print(answer[0], answer[1], answer[2])
