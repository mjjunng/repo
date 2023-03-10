# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):

    def solve(w, h):

        edgs = h*2
        upper = (brown-edgs)//2

        if upper*2 + edgs != brown:
            return 0

        width = w+2

        if upper % width:
            return 0

        height = (upper//width) * 2 + h

        return [width, height]

    for h in range(1, yellow+1):
        if yellow % h:
            continue

        w = yellow // h

        rst = solve(w, h)
        if rst == 0:
            continue
        return rst


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
