# https://school.programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers, target):
    def dfs(idx):
        nonlocal answer
        if idx == N:
            if sum(tmp) == target:
                answer += 1
            return

        tmp[idx] = numbers[idx]
        dfs(idx+1)
        tmp[idx] = -numbers[idx]
        dfs(idx+1)

    N = len(numbers)
    tmp = [0]*(N)
    answer = 0
    dfs(0)
    return answer


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))
