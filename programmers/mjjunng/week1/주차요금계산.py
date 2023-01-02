from collections import deque
import math


def cal(s1, s2):
    l1 = s1.split(":")
    l2 = s2.split(":")
    h1, m1 = l1[0], l1[1]
    h2, m2 = l2[0], l2[1]

    return abs((int(h1) * 60 + int(m1)) - (int(h2) * 60 + int(m2)))


def findq(num, q):
    for n, t in q:
        if n == num:
            return t
    return -1


def solution(fees, records):
    answer = []
    res = []
    q = deque()
    d = {}
    final = []
    for i in records:
        lst = i.split(" ")

        if lst[2] == "IN":
            q.append([lst[1], lst[0]])
        else:
            pre_t = findq(lst[1], q)
            q.remove([lst[1], pre_t])
            answer.append([lst[1], cal(pre_t, lst[0])])
    if len(q) > 0:
        for n, t in q:
            answer.append([n, cal(t, "23:59")])

    for n, t in answer:
        if n in d:
            d[n] += t
        else:
            d[n] = t

    for i in d:
        if fees[0] < d[i]:
            won = fees[1] + math.ceil((d[i] - fees[0]) / fees[2]) * fees[3]
            res.append([i, won])
        else:
            res.append([i, fees[1]])

    res.sort(key=lambda x: x[0])

    for n, t in res:
        final.append(t)

    return final
