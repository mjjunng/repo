n = int(input())
a = [[0]*100 for _ in range(100)]
p = [49, 49]    # 현재 위치
start = [49, 49]
end = [49, 49]
s = input()
d = 0   # 0: 아래쪽 1: 오른쪽 2: 위쪽 3: 왼쪽
i = 0

while i < n:
    if s[i] != "F":
        if s[i] == "R":
            d += 1
        elif s[i] == "L":
            d -= 1
    else:
        a[p[0]][p[1]] = "."
        if d % 4 == 0:
            p[0] += 1
            end[0] = max(p[0], end[0])
        elif d % 4 == 1:
            p[1] -= 1
            start[1] = min(p[1], start[1])
        elif d % 4 == 2:
            p[0] -= 1
            start[0] = min(p[0], start[0])
        elif d % 4 == 3:
            p[1] += 1
            end[1] = max(p[1], end[1])
    i += 1

a[p[0]][p[1]] = "."

for i in range(start[0], end[0]+1):
    for j in range(start[1], end[1]+1):
        if a[i][j] == 0:
            a[i][j] = "#"
        print(a[i][j], end="")
    print()