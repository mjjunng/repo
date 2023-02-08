# sol 1) 단순 구현: 72점 

def solution(scores):
    answer = 0
    lst = []
    tmp = scores[:]
    tmp.sort(key=lambda x:x[0])
    s = tmp[-1]
    
    tmp.sort(key=lambda x:x[1])
    s1 = tmp[-1]

    # 인센티브 받을 수 있는 직원만 리스트에 추가
    for i in range(len(scores)):
        a = scores[i][0]
        b = scores[i][1]
        if (a < s[0] and b < s[1]) or (a < s1[0] and b < s1[1]):
            if i == 0:
                return -1
            continue
        
        lst.append([a+b, i])
    
    # 등수 매기기 
    lst.sort(key=lambda x:x[0], reverse=True)
    
    if lst[0][1] == 0:
        return 1
    else:
        score = lst[0][0]
        rating = 1
        cnt = 0
        for i in range(1, len(lst)):
            if score == lst[i][0]:
                cnt += 1
            else:
                rating += cnt + 1
                cnt = 0
                score = lst[i][0]

            if lst[i][1] == 0:
                    return rating

