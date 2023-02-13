'''
** 핵심 : 빠른 검색(탐색)

1. querying 최적화 : hashing -> dictionary
2. 점수 충족 : 이진 탐색 (bisect 활용)
'''
from itertools import product, combinations
from bisect import bisect_left


def solution(info, query):
    # 존재하는 모든 조합에 대한 딕셔너리 초기화
    infos = dict()
    for x in product(['cpp', 'java', 'python', '-'], ['backend', 'frontend', '-'], ['junior', 'senior', '-'],
                     ['chicken', 'pizza', '-']):
        infos[x] = []

    # 해당 조합의 정보 담기 -> '-'도 고려하기 (0개 ~ 4개 집어 넣기)
    for x in info:
        x_lst = x.split()  # index 0 - 3 : 개발 언어, 직군, 경력, 소울 푸드 / 4 : 점수

        # 모든 조합에 대해 정보 추가
        for k in range(5):
            for c in combinations(range(4), k):  # c[i] -> '-'가 삽입될 인덱스
                tmp_x = x_lst[:-1]  # 복사
                for i in c:
                    tmp_x[i] = '-'
                infos[tuple(tmp_x)].append(int(x_lst[-1]))  # 해당 조합에 대해 점수 추가

    # 점수 배열 SORT
    for k in infos.keys():
        if infos[k]:
            infos[k].sort()

    # query 돌면서 이진 탐색 수행
    res = []
    for q in query:
        l, _, p, _, e, _, f, s = q.split()
        li = bisect_left(infos[(l, p, e, f)], int(s))
        res.append(len(infos[(l, p, e, f)]) - li)

    return res


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))
