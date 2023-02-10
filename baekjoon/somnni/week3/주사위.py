import sys
from itertools import combinations


# 주사위 m 면이 연결되어 있는지 확인
# 주사위 [1, 2, 3, 4, 5, 6] 이면
# 1 또는 6을 한 면으로 골랐을 때 6 또는 1이 올 수 없음
# 2, 5는 같이 올 수 없음
# 3, 4는 같이 올 수 없음
def check(m, c):
    for i in range(c):
        if m[i] == 0:
            if 5 in m:
                return False
        if m[i] == 1:
            if 4 in m:
                return False
        if m[i] == 2:
            if 3 in m:
                return False
        if m[i] == 3:
            if 2 in m:
                return False
        if m[i] == 4:
            if 1 in m:
                return False
        if m[i] == 5:
            if 0 in m:
                return False
    return True
n = int(input())
dice = list(map(int, input().split()))
# n = 1 일 때, 수가 제일 큰 것을 제외
if n == 1:
    dice.pop(dice.index(max(dice)))
    ans = sum(dice)
else:
    d = [0, 1, 2, 3, 4, 5]
    ans = 0
    # 연결된 세 개의 면의 합이 제일 작은 수로 채움
    # 총 4개 (정육면체 맨 위 측면 모서리)
    q = list(set(combinations(d, 3)))
    s = sys.maxsize
    for i in range(len(q)):
        if check(q[i], 3):
            tmp = 0
            q[i] = list(q[i])
            for j in range(len(q[i])):
                tmp += dice[q[i][j]]
            s = min(s, tmp)
    ans += s * 4
    # 연결된 두 면의 합이 제일 작은 수로 채움
    # 총 개 (정육면체 맨 위의 측면 모서리 제외하고 옆 측면 양 끝 + 맨 위의 양 끝)
    q = list(set(combinations(d, 2)))
    s = sys.maxsize
    for i in range(len(q)):
        if check(q[i], 2):
            tmp = 0
            q[i] = list(q[i])
            for j in range(len(q[i])):
                tmp += dice[q[i][j]]
            s = min(s, tmp)
    ans += s * ((n-1) * 4 + (n-2) * 4)
    # 제일 작은 수로 채움
    # 총 개 (정육면체 옆 측면 맨 아래를 제외한 양 끝 제외 + 맨 위의 측면 양 끝 제외)
    ans += min(dice) * ((n-2) * (n-1) * 4 + (n-2) * (n-2))
print(ans)