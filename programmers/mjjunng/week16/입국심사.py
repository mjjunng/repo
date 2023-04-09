def solution(n, times):
    lower = 1
    upper = max(times) * n
    
    while lower <= upper:
        mid = (lower + upper) // 2
        # 심사받는 사람의 수 
        people = 0
        for i in range(len(times)):
            # n분 // 입국 심사시 걸리는 시간 = n분 동안 입국 심사 받을 수 있는 사람의 수 
            people += mid // times[i]  
            
            if people >= n:
                break

        if people < n:
            lower = mid + 1
        else:
            answer = mid
            upper = mid - 1
            
    return answer
