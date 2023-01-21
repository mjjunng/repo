"""
그리디
- 3개 조합, 2개 조합, 1개 조합 중 최솟값을 뽑아서 블럭의 위치에 따라 연산

1st: 블럭의 위치에 따라(모서리, 변, 안쪽) 가장 작은 1 ~ 3개의 면의 뽑아서 계산 -> 틀린 접근: 전개도에 따른 조합을 고려 못했음
"""


def calc():
    if n == 1:
        return sum(sorted([A, B, C, D, E, F])[:5])

    total = 0
    # 모서리 - 3면
    total += 4 * top_three
    # 변 - 2면
    total += (n - 1) * 4 * top_two + (n - 2) * 4 * top_two
    # 나머지 안쪽 - 1면
    total += (n - 2) ** 2 * top_one + (n - 2) * (n - 1) * 4 * top_one

    return total


n = int(input())
A, B, C, D, E, F = map(int, input().split())  # 6면
top_three = min(A+B+C, A+B+D, A+C+E, A+D+E, B+C+F, B+D+F, E+D+F, C+E+F)
top_two = min(A+C, A+B, A+D, A+E, B+C, B+D, D+E, C+E, C+F, B+F, D+F, E+F)
top_one = min(A, B, C, D, E, F)

print(calc())
