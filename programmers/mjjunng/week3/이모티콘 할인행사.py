from itertools import product
    
def solution(users, emoticons):
    res = []
    sales = [10, 20, 30, 40]
    data = list(product(sales, repeat=len(emoticons)))
    
    for i in range(len(data)):
        total_price = 0     # 할인율별 모든 사용자의 이모티콘 총 합 
        total_cnt = 0   # 할인율별 이모티콘 플러스 서비스 가입 수
        for j in range(len(users)):
            price = 0   # 사용자별 구매하는 이모티콘의 총 합 
            for k in range(len(data[i])):
                # 이모티콘 구매할 수 있는지 확인 
                if users[j][0] <= data[i][k]:
                    price += emoticons[k] * (1-data[i][k]*0.01)
            # 이모티콘의 구매 바용이 일정 가격을 넘었다면, 이모티콘 플러스 서비스에 가입  
            if price >= users[j][1]:
                total_cnt += 1
                price = 0
                
            total_price += price
        res.append([total_cnt, total_price])   
    
    res.sort(key=lambda x:(-x[0], -x[1]))
        
    return res[0]
