# https://school.programmers.co.kr/learn/courses/30/lessons/42839

def solution(numbers):

    def solve(idx, n):

        if idx == N:
            if n == '':
                return
            n = int(n)
            if primes[n]:
                prime.add(n)
            return

        for i in range(N):
            if vis[i]:
                continue

            vis[i] = True
            solve(idx+1, n+numbers[i])
            solve(idx+1, n)
            vis[i] = False

    N = len(numbers)
    mx = int(''.join(sorted(numbers, reverse=True))) + 10
    primes = [True] * (mx)
    primes[0] = primes[1] = False
    i = 2
    while i*i <= mx:
        if primes[i] == False:
            i += 1
            continue

        j = i*i
        while j < mx:
            primes[j] = False
            j += i
        i += 1

    vis = [False] * N
    prime = set()
    solve(0, "")

    return len(prime)


"""
에르토스테네스의 체
dfs
"""
