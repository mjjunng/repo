"""
** 그리디
- 가장 긴 변 가로 or 세로로 고정 (기준점 설정)
- 전체 돌면서 더 긴 변은 기준점으로 몰아주기 (SWAP 수행)
"""


# 가로 MAX, 세로 MAX 구해서 반환
def get_max(sizes):
    return max(list(map(lambda x: x[0], sizes))), max(list(map(lambda x: x[1], sizes)))


def solution(sizes):
    max_w, max_h = get_max(sizes)
    p = 0 if max_w > max_h else 1  # 기준점 -> 긴 변은 다 가로 or 세로로 몰아주기

    for size in sizes:
        # SWAP
        if (p == 0 and size[0] < size[1]) or (p == 1 and size[0] > size[1]):
            size[0], size[1] = size[1], size[0]
    max_w, max_h = get_max(sizes)

    return max_w * max_h

