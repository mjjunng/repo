# https://school.programmers.co.kr/learn/courses/30/lessons/154539

def solution(numbers):
    N = len(numbers)
    answer = [-1] * N
    stack = []
    for i in range(N):
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()
            answer[idx] = numbers[i]
        stack.append(i)

    return answer


print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))
