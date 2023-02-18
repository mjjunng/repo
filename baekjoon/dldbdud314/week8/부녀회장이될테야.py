'''
2775. 부녀 회장이 될테야
단순 구현
'''

T = int(input())
res = []
for _ in range(T):
    k = int(input())  # 층
    n = int(input())  # 호

    floors = [[0] * (n + 1) for _ in range(k + 1)]
    floors[0] = [m for m in range(n + 1)]  # 0층
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            floors[i][j] = sum(floors[i - 1][1:j + 1])

    res.append(floors[k][n])

print(*res, sep='\n')
