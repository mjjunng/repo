'''
구현
time: 중복순열 & inner loops -> O(4^m * n * m)

- [10, 20, 30, 40]에서 중복 순열로 m개를 뽑아서,
- 각각의 임티 할인률 적용 조합에 대해 가입자 수, 총 구매 가격 계산
- [가입자 수, 총 구매 가격 계산] max 갱신
'''
from itertools import product


def solution(users, emoticons):
    res = [-int(1e9), -int(1e9)]  # 최종 결과 [가입자 수, 임티 가격] : 갱신 대상

    for sales in product([10, 20, 30, 40], repeat=len(emoticons)):
        joined = 0  # 해당 조합일 때 가입자 수
        price = 0  # 해당 조합일 때 구매 임티 가격

        for user in users:
            user_buy_price = 0  # 사용자별 구매 임티 가격
            user_sale, user_join = user[0], user[1]  # 사용자 구매/가입 기준치
            for i, sale in enumerate(sales):
                if sale >= user_sale:
                    user_buy_price += emoticons[i] * (1 - sale / 100)
            # 가입여부, 총 구매가격 최대치 갱신
            if user_buy_price >= user_join:
                joined += 1
                user_buy_price = 0
            price += user_buy_price

        res = max(res, [joined, price])

    return res


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))