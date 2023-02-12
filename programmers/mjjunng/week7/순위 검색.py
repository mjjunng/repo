# 풀이 참고: https://www.youtube.com/watch?v=vFwVvJQnC4M

from collections import defaultdict

def solution(info, query):
    answer = [0 for _ in range(len(query))]
    d = defaultdict(list)
    
    # info를 기반으로 딕셔너리를 만든다.   
    for i in info:
        data = i.split(" ")
        langs = [data[0], "-"]
        jobs = [data[1], "-"]
        exps = [data[2], "-"]
        foods = [data[3], "-"]
        val = int(data[4])
        
        for lang in langs:
            for job in jobs:
                for exp in exps:
                    for food in foods:
                        key = lang + " " + job + " " + exp + " " + food
                        d[key].append(val)
    # 저장한 코딩테스트 점수 정렬 
    # --> 해당 딕셔너리의 값이 이후에 변경될 일 없기 때문에, 최적화한 상태 유지
    for item in d:
        d[item].sort()
        
    # 쿼리에 해당하는 사람 counting
    idx = 0
    for q in query:
        data = q.split(" and ")
        key = data[0] + " " + data[1] + " " + data[2] + " " + data[3].split(" ")[0]
        score = int(data[3].split(" ")[1])
        
        if key in d:
            # binary search를 통해 해당 점수보다 큰 점수를 가진 지원자를 찾는다 
            lower = 0
            upper = len(d[key])
            while lower < upper:
                mid = (lower + upper) // 2
                if d[key][mid] >= score:
                    upper = mid
                else:
                    lower = mid+1
            answer[idx] = len(d[key]) - lower   # 쿼리에 해당하는 전체 지원자수-해당 점수 이상인 지원자의 인덱스값
        idx += 1
            
    return answer
