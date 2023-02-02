import sys
from itertools import combinations
'''
    첫 번째 풀이 방법: 완전 탐색  -> 시간 초과 
    첫 번째 집부터 마지막 집까지 for문 돌면서 갈 수 있는 치킨집 다 가봄 
    단, 갔던 치킨집을 리스트에 저장해놓고 이전에 갔던 집이면 카운트 안 함 
    마지막 집까지 다 돌고 갔던 치킨집의 개수가 m이하라면 값 갱신  
'''


def calculate(house_y, house_x, chicken_y, chicken_x):
    return abs(chicken_y-house_y) + abs(chicken_x-house_x)

def dfs(lev, dis, visited):
    global res

    # 이미 방문한 치킨 집의 수가 m보다 크다면, 더이상 탐색할 필요가 없기 때문에 종료
    if len(visited) > m:
        return

    if lev == len(houses):
        if len(visited) <= m:
            if dis < res:
                res = dis
        return

    for i in chickens:
        tmp = visited[:]
        if i in tmp:
            dfs(lev+1, dis+calculate(houses[lev][0], houses[lev][1],
                                          i[0], i[1]), tmp)
        else:
            tmp.append(i)
            dfs(lev+1, dis+calculate(houses[lev][0], houses[lev][1],
                                          i[0], i[1]), tmp)

if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    n, m = map(int, input().split())
    board = []
    houses = []
    chickens = []
    res = float('inf')

    for _ in range(n):
        board.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                houses.append([i, j])
            elif board[i][j] == 2:
                chickens.append([i, j])
    dfs(0, 0, [])

    print(res)

'''
    두 번째 풀이 방법: 조합을 이용한 완전 탐색 
     
'''

if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    n, m = map(int, input().split())
    board = []
    houses = []
    chickens = []
    res = float('inf')

    for _ in range(n):
        board.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                houses.append([i, j])
            elif board[i][j] == 2:
                chickens.append([i, j])

    for i in combinations(chickens, m):   # 치킨집 중 m개 선택한 모든 경우의 수
        tmp = 0 # 모든 집의 치킨 거리
        for house in houses:
            # 고른 치킨집 중 집에서 가장 가까운 치킨집까지의 거리
            min_dis = float('inf')
            for chicken in i:
                min_dis = min(min_dis, calculate(house[0], house[1],
                                                 chicken[0], chicken[1]))
            tmp += min_dis
        res = min(res, tmp)

    print(res)
