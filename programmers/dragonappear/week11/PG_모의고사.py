# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):

    N = len(answers)

    a = [1, 2, 3, 4, 5] * N
    b = [2, 1, 2, 3, 2, 4, 2, 5] * N
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * N

    rst = [0, 0, 0]

    for i in range(N):
        if a[i] == answers[i]:
            rst[0] += 1
        if b[i] == answers[i]:
            rst[1] += 1
        if c[i] == answers[i]:
            rst[2] += 1

    ans = []
    mx = max(rst)
    for i in range(3):
        if mx == rst[i]:
            ans.append(i+1)

    return ans


print(solution([1, 2, 3, 4, 5]))
