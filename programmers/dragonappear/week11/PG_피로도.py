# https://school.programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations


def solution(k, dungeons):

    N = len(dungeons)
    mx = -1
    for p in permutations([i for i in range(N)]):
        tmp = k
        cnt = 0

        for i in p:
            least, consume = dungeons[i]
            if least > tmp:
                break

            cnt += 1
            tmp -= consume

        mx = max(cnt, mx)
    return mx


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
