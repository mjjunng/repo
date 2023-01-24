'''
y <= (d의 제곱 + x의 제곱)의 루트 임을 이용해
x 좌표에 대해 단일 for loop
'''


def solution(k, d):
    # x가 i일 때 y의 최대치를 구해서 개수 갱신
    total = 0
    for i in range(0, d + 1, k):
        max_y = (d ** 2 - i ** 2) ** 0.5
        total += int(max_y) // k + 1

    return total


print(solution(1, 5))  # 26
