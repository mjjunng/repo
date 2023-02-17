n, m = map(int, input().split())
arr = [0 * m for i in range(n)]
for i in range(n):
    arr[i] = list(map(int, input()))

result = 0

for i in range(n):
    for j in range(m):
        if i > 0 and j > 0 and arr[i][j]:
            if arr[i][j]:
                arr[i][j] += min(arr[i][j-1], arr[i-1][j], arr[i-1][j-1])
    result = max(result, max(arr[i]))
print(result*result)
