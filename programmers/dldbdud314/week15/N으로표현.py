"""
** DP + 완탐 아이디어

cnt = N을 사용한 횟수, DP[cnt] = set() -> N을 cnt개 활용해서 만들 수 있는 숫자 SET
cnt 1 ~ 8까지 연산하며, number 일치하는 set이 나오면 바로 cnt RETURN

한 라운드 당 SET: operate(dp[i], dp[cnt - i]) + N을 cnt개 이어붙인 숫자
"""
from itertools import product


def operate(s1, s2):  # 연산 메소드
    to_add = set()
    for n1, n2 in product(s1, s2):
        to_add.add(n1 + n2)
        to_add.add(n1 - n2)
        to_add.add(n1 * n2)
        if n2 != 0: to_add.add(n1 // n2)
    return to_add


def solution(N, number):
    if N == number:  # 바로 RETURN
        return 1

    dp = [None] * 9
    dp[1] = {N}  # N을 cnt개 사용해서 만들 수 있는 숫자 SET

    for cnt in range(2, 9):  # 최대 8까지
        dp[cnt] = {int(str(N) * cnt)}
        for i in range(1, cnt):
            dp[cnt].update(operate(dp[i], dp[cnt - i]))
        if number in dp[cnt]:
            return cnt

    return -1
