"""
** 스택 : 아이디어 참고
"""


def solution(numbers):
    stack = []
    ans = [-1] * len(numbers)
    for idx in range(len(numbers)):
        # stack top 보다 큰 수가 등장하면 뒷 큰 수 갱신
        while stack and stack[-1][0] < numbers[idx]:
            _, _idx = stack.pop()
            ans[_idx] = numbers[idx]

        stack.append((numbers[idx], idx))

    return ans
