# https://www.acmicpc.net/problem/11066
# 참고: https://data-make.tistory.com/402
from sys import stdin
input = stdin.readline


for _ in range(int(input())):
    N, A = int(input()), [0] + list(map(int, input().split()))
    S = [0 for _ in range(N+1)]  # S[i]는 1번부터 i번까지의 누적합
    for i in range(1, N+1):
        S[i] = S[i-1]+A[i]

    # d[i][j]: i에서 j까지 합하는데 필요한 최소 비용
    # d[i][k] + d[k+1][j] + sum(A[i]~A[j])
    d = [[0] * (N+1) for _ in range(N+1)]
    for i in range(2, N+1):  # 부분 파일의 길이
        for j in range(1, N+2-i):  # 시작점
            d[j][j+i-1] = min([d[j][j+k] + d[j+k+1][j+i-1]
                              for k in range(i-1)]) + (S[j+i-1] - S[j-1])

    print(d[1][N])
