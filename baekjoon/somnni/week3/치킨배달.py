import sys

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
# 모든 집
house = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            house.append((i,j))
# 모든 치킨집
chicken = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            chicken.append((i,j))
# 모든 치킨집에 대해서 모든 집 사이의 거리
distance = {}
for i in range(len(chicken)):
    distance[chicken[i]] = {}
    for j in range(len(house)):
        distance[chicken[i]][house[j]] = abs(chicken[i][0] - house[j][0]) + abs(chicken[i][1] - house[j][1])


# 치킨거리가 제일 작은 경우의 수를 구한다
# m 치킨집이 있어야 한다 (제거 안 할 치킨집의 수 = c)
def smallest_distance(arr):
    r = [] * len(house)
    h = list(house)
    for i in range(len(house)):
        tmp = []
        for j in arr:
            tmp += [distance[j][h[i]]]
        r.append(min(tmp))
    return sum(r)


def solution(arr, c, i):
    if m == c:
        s = smallest_distance(arr)
        if s < ans[0]:
            ans[0] = s
        return
    if i >= len(chicken):
        return
    solution(arr, c, i+1)
    solution([chicken[i]] + arr, c + 1, i+1)

ans = [sys.maxsize]
solution([], 0, 0)
print(ans[0])