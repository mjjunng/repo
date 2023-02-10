from itertools import permutations
import copy


def blocks(n, m, a, r, c, cmd):
    block = []
    # 오른쪽
    # 가로 방향을 기준으로 c+1 지점부터 m 지점까지 봐주면 된다
    if cmd == 0:
        i = c + 1
        while i < m and a[r][i] != 6:
            if a[r][i] == 0:
                block.append([r, i])
            i += 1
    # 왼쪽
    # 가로 방향을 기준으로 c-1 지점부터 0 지점까지 봐주면 된다
    elif cmd == 1:
        i = c - 1
        while i >= 0 and a[r][i] != 6:
            if a[r][i] == 0:
                block.append([r, i])
            i -= 1
    # 아래쪽
    # 세로 방향을 기준으로 r+1 지점부터 n 지점까지 봐주면 된다
    if cmd == 2:
        i = r + 1
        while i < n and a[i][c] != 6:
            if a[i][c] == 0:
                block.append([i, c])
            i += 1
    # 위쪽
    # 가로 방향을 기준으로 r-1 지점부터 m 지점까지 봐주면 된다
    elif cmd == 3:
        i = r - 1
        while i >= 0 and a[i][c] != 6:
            if a[i][c] == 0:
                block.append([i, c])
            i -= 1
    return block


def solution(n, p, a, k):
    ans = 0
    for i in range(len(k)):
        r = k[i] // p
        c = k[i] % p
        m1 = blocks(n, p, a, r, c, 0)
        m2 = blocks(n, p, a, r, c, 1)
        m3 = blocks(n, p, a, r, c, 2)
        m4 = blocks(n, p, a, r, c, 3)
        if a[r][c] == 1:
            m = m1
            for j in [m2, m3, m4]:
                # 최대 감시 구역 크기 비교
                if len(m) < len(j):
                    m = j
        elif a[r][c] == 2:
            # 오른쪽, 왼쪽
            d1 = m1 + m2
            # 위쪽, 아래쪽
            d2 = m4 + m3
            m = d1
            # 최대 감시 구역 크기 비교
            if len(m) < len(d2):
                m = d2
        elif a[r][c] == 3:
            # 오른쪽, 위쪽
            d1 = m1 + m4
            # 오른쪽, 아래쪽
            d2 = m1 + m3
            # 왼쪽, 아래쪽
            d3 = m2 + m3
            # 왼쪽, 위쪽
            d4 = m2 + m4
            m = d1
            for j in [d2, d3, d4]:
                # 최대 감시 구역 크기 비교
                if len(m) < len(j):
                    m = j
        elif a[r][c] == 4:
            # 오른쪽, 위쪽, 왼쪽
            d1 = m1 + m4 + m2
            # 오른쪽, 아래쪽, 위쪽
            d2 = m1 + m3 + m4
            # 왼쪽, 아래쪽, 오른쪽
            d3 = m2 + m3 + m1
            # 왼쪽, 위쪽, 아래쪽
            d4 = m2 + m4 + m3
            m = d1
            for j in [d2, d3, d4]:
                # 최대 감시 구역 크기 비교
                if len(m) < len(j):
                    m = j
        elif a[r][c] == 5:
            # 오른쪽, 왼쪽
            m = m1 + m2 + m3 + m4
        # m 은 최대 감시 구역을 갖고 있는 경우
        # 방문한 감시 구역 제외한 감시 구역 수 구하기
        for j in m:
            ans += 1
            # 감시 구역 방문 기록하기
            a[j[0]][j[1]] = -1
    return ans


n, m = map(int, input().split())
a = [0]*n
d = []
l = 0
for i in range(n):
    a[i] = list(map(int, input().split()))
    for j in range(m):
        if a[i][j] != 0:
            l += 1
            if a[i][j] != 6:
                d.append(i*m+j)
# 모든 경우의 수
d = list(permutations(d))
# 최대를 찾기 위해 ans 는 최소 크기인 0으로 초기화
ans = 0
for i in range(len(d)):
    # d[i] 에 최대 감시 구역 크기를 담기
    d[i] = solution(n, m, copy.deepcopy(a), d[i])
    # 최대 크기 찾기
    if d[i] > ans:
        ans = d[i]
# 전체 블락 수에서 벽, CCTV, 감시 구역 크기를 빼준다
print(n*m - l - ans)