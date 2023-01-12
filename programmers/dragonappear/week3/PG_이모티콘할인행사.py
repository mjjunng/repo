# https://school.programmers.co.kr/learn/courses/30/lessons/150368
from typing import List

# 완전탐색
def solution(users, emoticons):

    # 이모티콘 할인율 구하기
    def dfs(discovered:List, depth):
        if depth == len(discovered):
            discounts.append(discovered[:])
            return
        for rate in rates:
            discovered[depth] += rate
            dfs(discovered, depth + 1)
            discovered[depth] -= rate
    
    answer = [0, 0]
    rates = [10 ,20, 30, 40]
    discounts = []
    # 이모티콘 수열 구하기
    dfs([0]*len(emoticons),0)
    
    # 완전탐색
    for discount_index in range(len(discounts)):
        join:int = 0 
        price:List = [0] * len(users)

        for emoticon_index in range(len(emoticons)):
            for user_index in range(len(users)):
                # 할인율 체크
                if users[user_index][0] <= discounts[discount_index][emoticon_index]:
                    price[user_index] += emoticons[emoticon_index] *  (100 - discounts[discount_index][emoticon_index]) / 100
        
        # 가입자 수 업데이트
        for user_index in range(len(users)):
            if price[user_index] >= users[user_index][1]:
                join += 1
                price[user_index] = 0
        
        # 가입자수, 금액 업데이트
        if join > answer[0]:
            answer[0] = join
            answer[1] = sum(price)
        elif join == answer[0]:
            answer[1] = max(answer[1], sum(price))

    return answer


users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
print(solution(users,emoticons))

