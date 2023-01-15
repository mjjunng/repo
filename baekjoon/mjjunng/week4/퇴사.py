'''
    첫 번째 풀이방법: dp 
    문제를 아예 잘못 이해함
    예를 들어, 6일에 걸리는 기간 1이라고 가정 
    그러면 다음 상담일이 무조건 7일이여야 한다고 생각함
    -> 7일 이후 모든 상담 가능함 
'''
if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    n = int(input())
    data = [[0, 0]]
    dp = [0 for _ in range(n+2)]   #dp[n]: n일까지 일했을 때 얻는 최대 수익
    res = 0

    for _ in range(n):
        data.append((list(map(int, input().split()))))

    for i in range(1, n+1):
        nxt = i + data[i][0]  # i일의 상담이 걸리는 시간

        if nxt <= n+1:  # 퇴사일 전까지 상담이 가능하다면, 최대 수익 갱신
            dp[nxt] = max(dp[nxt], dp[i] + data[i][1])
    print(max(dp))

'''
    두 번째 풀이방법: dp 
'''
if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    n = int(input())
    data = [[0, 0]]
    dp = [0 for _ in range(n+2)]
    res = 0

    for _ in range(n):
        data.append((list(map(int, input().split()))))

    for i in range(1, n+1):
        nxt = i + data[i][0]
        # 다음 상담이 가능한 모든 상담 일자의 dp값 갱신
        for j in range(nxt, n+2):
            dp[j] = max(dp[j], dp[i] + data[i][1])

    print(dp[n+1])
