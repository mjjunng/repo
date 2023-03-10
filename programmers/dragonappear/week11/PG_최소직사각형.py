# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):

    for size in sizes:
        size.sort()

    sizes.sort()
    lt = sizes[-1][0]

    sizes.sort(key=lambda x: x[1])
    rt = sizes[-1][1]

    return lt * rt


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
