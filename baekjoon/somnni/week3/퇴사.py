import sys


def solution(d, s, prev):
    if d > n:
        return s - prev
    if d == n:
        return s
    ans = -sys.maxsize
    for i in range(d, n):
        ans = max(ans, solution(i + days[i], s + price[i], price[i]))
    return ans


n = int(input())
days = [0] * n
price = [0] * n
for i in range(n):
    days[i], price[i] = map(int, input().split())
print(solution(0, 0, 0))