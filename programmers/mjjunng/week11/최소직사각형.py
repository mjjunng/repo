def solution(sizes):
    answer = 0
    b = []  # w와 h 비교해서 더 큰 길이 저장 
    s = []  # 더 작은 길이 저장 
    
    
    for w, h in sizes:
        if w >= h:
            b.append(w)
            s.append(h)
        else:
            b.append(h)
            s.append(w)
    
    return max(b) * max(s)
