"""
** 백트래킹(dfs) -> 순열 구현 (완전 탐색)
- dfs 돌면서 소수인지 판별 후 반영
"""
from math import sqrt

primes = set()  # 소수 결과 SET (중복된 소수 제거)


def is_prime(number):  # 소수 판별
    if number == 0 or number == 1:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def dfs(visited, cur_lst, numbers):
    global primes
    if cur_lst:
        if cur_lst[0] == "0":  # 0으로 시작 -> cut-edge
            return
        # 소수인지 판별 하고 반영
        cur_num = int(''.join(cur_lst))
        if is_prime(cur_num):
            primes.add(cur_num)

    for i in range(len(numbers)):
        if not visited[i]:
            visited[i] = True
            dfs(visited, cur_lst + [numbers[i]], numbers)
            visited[i] = False


def solution(numbers):
    dfs([False] * len(numbers), [], numbers)  # 방문 여부, 해당 문자 담은 배열 (현재 배열), numbers
    return len(primes)

