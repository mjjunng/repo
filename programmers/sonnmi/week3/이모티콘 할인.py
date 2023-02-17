from itertools import combinations


def solution(users, emoticons):
    answer = []
    mx_cnt = 0
    mx_price = 0
    q = list(set(combinations([0.1, 0.2, 0.3, 0.4] * len(emoticons), len(emoticons))))
    q.sort()
    # 모든 이모티콘에 10, 20, 30, 40% 할인 해보고 최대를 찾는다
    for i in range(len(q)):
        price = 0
        cnt = 0
        for user in users:
            sell_price = 0
            rate = user[0] / 100
            for j in range(len(emoticons)):
                if q[i][j] >= rate:
                    sell_price += emoticons[j] * (1 - q[i][j])
            p = user[1]
            if sell_price >= p:
                cnt += 1
            else:
                price += sell_price
        # 유저 사용 수가 더 우선으로 비교한다
        # 수가 같다면 mx_price 비교한다
        if cnt > mx_cnt:
            mx_cnt = cnt
            mx_price = price
        elif cnt == mx_cnt:
            if price > mx_price:
                mx_cnt = cnt
                mx_price = price
    answer = [mx_cnt, int(mx_price)]
    return answer