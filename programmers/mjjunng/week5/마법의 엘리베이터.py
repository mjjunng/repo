# 구현 O(n)

def solution(storey):
    answer = 0
    
    while storey:
        re = storey % 10    # 마지막 자릿값 
        print(re)
        # 현재 자릿값이 6~9 -> 10에 도달 
        if 6 <= re <= 9:
            answer += 10 - re
            storey += 10 - re
            
        # 현재 자릿값이 0~4 -> 0에 도달 
        elif 0 <= re <= 4:
            answer += re
        
        # 현재 자릿값이 5 
        # 다음 자릿값이 5~9 -> 현재 자릿값을 10에 도달  
        # 다음 자릿값이 0~4 -> 현재 자릿값을 0에 도달  
        else:
            if 5 <= (storey // 10) % 10:
                answer += 10 - re
                storey += 10 - re
            else:
                answer += re
                
        storey //= 10
    return answer
