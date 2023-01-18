"""
구현

<<전처리>>
- 집 위치, 치킨집 위치 리스트 저장하기
- 각각의 집마다 각각의 치킨집까지의 거리 연산하기
<<메인>>
- 전체 치킨집에서 m개 뽑아서 (combinations 활용)
- 각각의 집들에 대해, 살아 남은 m개의 치킨집들 중 최소값 뽑아서 더하기 (치킨거리 연산) -> total
- total 중 최소값 return
"""
from itertools import combinations

n, m = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]

# 집과 치킨집의 위치 저장
houses, chickens = [], []  # 집 위치, 치킨집 위치 리스트
for i in range(n):
    for j in range(n):
        if MAP[i][j] == 1:
            houses.append((i, j))
        elif MAP[i][j] == 2:
            chickens.append((i, j))

# 각각의 집마다 각각의 치킨집까지의 거리 구하기
chicken_distances = []
for house in houses:
    hx, hy = house
    tmp = []
    for cx, cy in chickens:
        d = abs(hx-cx) + abs(hy-cy)
        tmp.append(d)  # i번째 치킨집과의 거리 저장
    chicken_distances.append(tmp)

# 전체 치킨집에서 m개를 뽑았을 때 (combinations)
# 각각의 집마다 살아 남은 치킨집 m개 중 최소값(=치킨거리)를 뽑아서
# 전체(total, 도시의 치킨거리)에 더하기 -> 그 중 최소값 구하기
min_total = float('inf')
for indexes in combinations(range(len(chickens)), m):
    cur_total = 0  # 해당 조합(m개의 치킨집 선정)에서의 거리 합
    for chicken_distance in chicken_distances:
        dset = []
        for i in range(len(chicken_distance)):
            if i in indexes:
                dset.append(chicken_distance[i])
        cur_total += min(dset)  # m개의 치킨거리 중 최솟값 더하기
    min_total = min(min_total, cur_total)

print(min_total)
