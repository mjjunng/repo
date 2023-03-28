from collections import deque
from copy import deepcopy

# 한 개의 알파벳만 다른 경우 -> 해당 인덱스 return, 이외의 경우 -1 return 
def find_diff(s1, s2):
    cnt = 0
    diff_idx = -1
    
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt += 1
            diff_idx = i
    
    if cnt == 1:
        return diff_idx
    else:
        return -1
            

def solution(begin, target, words):
    answer = float('inf')
    n = len(begin)
    q = deque()
    q.append([begin, 0, set()])    # 바꾼 문자열, 횟수, 방문한 word 저장용 set 
    
    while q:
        now, cnt,visited = q.popleft()
        
        if now == target:   # 현재 pop한 문자열이 target인 경우 -> 최소값이므로 바로 break 
            answer = cnt
            break
            
        for word in words:
            idx = find_diff(now, word)  
            v = deepcopy(visited)
            
            if idx != -1 and word not in v: # 한 개의 알파벳만 다르고, 이전에 탐색하지 않은 경우 
                new_str = now[:idx] + word[idx] + now[idx+1:]   # 변환
                v.add(word)
                q.append([new_str, cnt+1, v])
    
    if answer == float('inf'):
        return 0
    
    return answer
