from itertools import permutations

def solution(k, dungeons):
    answer = 0
    cases = permutations(dungeons)
    
    for c in cases:
        now = k
        cnt = 0
        for stage in c:
            if stage[0] <= now:
                now -= stage[1]
                cnt += 1
            else:
                break
                
        answer = max(answer, cnt)
    
    return answer
