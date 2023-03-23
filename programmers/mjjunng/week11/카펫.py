def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for i in range(3, total//2+1): 
        if total % i == 0:
            w = i
            h = total // i
            y = (w-2) * (h-2)
            
            if y == yellow and total - y == brown:
                answer.append(max(w, h))
                answer.append(min(w, h))
                break
    return answer
