import itertools
import math

def solution(numbers):
    answer = 0
    all_numbers = set()

    # 주어진 숫자로 구할 수 있는 모든 수 - 순열 
    for i in range(1, len(numbers)+1):
        tmp = itertools.permutations(numbers, i)

        for j in tmp:
            all_numbers.add(int("".join(j)))

    # 소수인지 판별
    for i in all_numbers:
        if isPrimeNum(i):
            answer += 1

    return answer

def isPrimeNum(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
