# sol 1) 구현: 76점 

def solution(scores):
    answer = 0
    lst = []
    tmp = scores[:]
    tmp.sort(key=lambda x:(x[0], x[1]))
    s = tmp[-1]     # 근무 태도가 가장 높은 사람 
    
    tmp.sort(key=lambda x:(x[1], x[0]))
    s1 = tmp[-1]    # 동료 평가가 가장 높은 사람 

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


# sol 2) 구현 - test case 3개 시간초과 발생 
def solution(scores):
    answer = 0
    vals = [] # 완호보다 높은 점수 받은 사원
    w_s1 = scores[0][0]
    w_s2 = scores[0][1]
    
    for i in range(len(scores)):
        if scores[i][0] + scores[i][1] >= scores[0][0] + scores[0][1]:
            vals.append([scores[i][0], scores[i][1], i])
    
    vals.sort(key=lambda x:x[0], reverse=True) # 근무 태도 점수 기준 내림차순 
    # 자기보다 앞에 있는 사원하고만 비교하면 된다 
    for i in range(len(vals)):
        a = vals[i][0]
        b = vals[i][1]
        idx = vals[i][2]
        check = 1
        for j in range(i):
            c = vals[j][0]
            d = vals[j][1]
            if a < c and b < d:
                if idx == 0:
                    return -1
                check = 0
                break
        if check == 0:
            continue
        else:  # 인센티브 받을 수 있는 직원
            if idx != 0:
                if a + b > w_s1 + w_s2:     # 원호보다 점수가 더 높은 사람만 count
                    answer += 1
    return answer + 1
    
    
# sol 3) 구현: 통과!  
# 두 번 정렬로 O(n)으로 비교 가능 

def solution(scores):
    answer = 1
    wonho_score = scores[0]
    scores.sort(key=lambda x:(-x[0], x[1]))
    pre = 0 # 이전 동료 평가 점수 
    
    for i in scores:
        if i[1] < pre:   
            if i == wonho_score:
                return -1
            continue
            
        pre = i[1]
        
        if i[0] + i[1] > wonho_score[0] + wonho_score[1]:
            answer += 1
        
   
    return answer

