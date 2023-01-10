# https://school.programmers.co.kr/learn/courses/30/lessons/118667
from collections import deque
from typing import List

# dfs
# 런타임 에러
mn = float('inf')
def solution(queue1, queue2):

    def dfs(q1:deque,q2:deque,sum_1,count:int):
        global mn

        if count < 0:
            return
        
        sum_2 = total_sum-sum_1
        if sum_1 == sum_2:
            mn = min(mn,max_operation*2-count)
            return 
        
        if len(q2)>0 and sum_2>sum_1:
            q1.append(q2.popleft())
            dfs(q1,q2,sum_1+q1[-1],count-1)
            q2.appendleft(q1.pop())
        elif len(q1)>0 and sum_2<sum_1:
            q2.append(q1.popleft())
            if sum_1-q2[-1]>0:
                dfs(q1,q2,sum_1-q2[-1],count-1)
            q1.appendleft(q2.pop())
    
    # 예외처리
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    total_sum = q1_sum + q2_sum
    if (q1_sum+q2_sum) % 2 != 0:
        return -1
    if q1_sum == q2_sum:
        return 0

    max_operation = len(queue1)+len(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)
    dfs(q1,q2,q1_sum,max_operation*2)

    if mn==float('inf'):
        return -1
    else:
        return mn

queue1 = [1,1]
queue2 = [1,5]
print(solution(queue1,queue2))


# greedy
def solution_2(queue1,queue2):
    answer = -1
    max_operation = len(queue1) + len(queue2)

    q1,q2 = deque(queue1),deque(queue2)
    sum1,sum2 = sum(q1),sum(q2)

    for cnt in range(max_operation*2):
        if sum1 == sum2:
            answer = cnt
            break
        elif sum1>sum2:
            item = q1.popleft()
            sum1 -= item
            q2.append(item)
            sum2 += item
        else:
            item = q2.popleft()
            sum2 -= item
            q1.append(item)
            sum1 += item
    
    return answer
