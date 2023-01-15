#첫 번째 풀이 방법: deque를 이용해서 두 큐의 합이 같아질 때까지 원소 pop, append -> 시간초과

from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    if (sum(queue1) + sum(queue2)) % 2 != 0:
        return -1
    
    while sum(q1) != sum(q2):
        if sum(q1) > sum(q2):
            q2.append(q1.popleft())
        else:
            q1.append(q2.popleft())
        answer += 1
        
        if answer > len(queue1) * 4:
            return -1
            
    

    return answer
    
    
#두 번째 풀이 방법: sum메서드 사용x -> +, -로 대체

from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    s1 = sum(queue1)
    s2 = sum(queue2)
    
    # 모두 더한 값이 홀수일 때는 어떠한 경우도 합이 같을 수 없음 
    if (s1 + s2) % 2 != 0:
        return -1
    
    # 합이 큰 큐 -> 합이 작은 큐로 원소 이동 
    while s1 != s2:
        if s1 > s2:
            num = q1.popleft()
            q2.append(num)
            s1 -= num
            s2 += num
        else:
            num = q2.popleft()
            q1.append(num)
            s2 -= num
            s1 += num
        answer += 1
        
        if answer > len(queue1) * 4:
            return -1

    return answer
