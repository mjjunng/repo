'''
구현 - 그리디

해당 구간의 최소 개수 식 (k는 해당 구간의 건물의 개수)
- 나누어 떨어지는 경우: k // (2 * w + 1)
- 나누어 떨어지지 않는 경우: k // (2 * w + 1) + 1
'''


def solution(n, stations, w):
    blanks = []  # 빈 공간 길이 담기 !
    tmp = 1  # 시작 (포함)
    for station in stations:  # 경계값 처리 유의..
        ss, se = station - w, station + w  # 시작/끝 포함 구간
        if ss > tmp:
            blanks.append(ss - tmp)
        tmp = se + 1
    if tmp <= n:  # 끝 처리
        blanks.append(n - tmp + 1)

    # 해당 빈 구간에 세울 수 있는 기지국의 최소 개수 구하기
    cnt = 0
    for k in blanks:
        cnt += k // (2 * w + 1) if k % (2 * w + 1) == 0 else k // (2 * w + 1) + 1

    return cnt
