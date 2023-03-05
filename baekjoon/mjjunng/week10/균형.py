# dp: O(n)

if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    t = int(input())
    dp = [0 for _ in range(44)]  # 높이가 n일 때 필요한 최소 노드의 개수

    dp[1] = 1
    for i in range(2, len(dp)):
        dp[i] = dp[i - 2] + dp[i - 1] + 1

    for _ in range(t):
        n = int(input())

        for i in range(len(dp)):
            if dp[i] > n:
                print(i-1)
                break

