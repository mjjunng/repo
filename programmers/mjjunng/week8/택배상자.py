# deque O(n)

from collections import deque


def solution(order):
    answer = 0
    n = len(order)
    q = deque([i for i in range(1, n + 1)]) # 컨테이너 벨트 
    tmp_q = deque() # 보조 컨테이너 벨트 

    for i in order:
        if q:
            # 컨테이너 벨트의 상자가 현재 순서가 될 때까지 보조 컨테이너에 쌓음 
            while q[0] < i: 
                tmp_q.append(q.popleft())
            
            # 컨테이너 벨트의 상자가 현재 순서가 되면, 컨테이너 벨트에서 pop
            if q[0] == i:
                q.popleft()
                answer += 1
                continue
        # 보조 컨테이너 벨트의 상자가 현재 순서가 되면, 보노 컨테이너 벨트에서 pop
        if tmp_q:
            if tmp_q[-1] == i:
                tmp_q.pop()
                answer += 1
                continue
                
        # 컨테이너 벨트의 0번째, 보조 컨테이너 벨트의 마지막에 해당 상자가 없다면, 
        # 상자 실을 수 없음 
        if q and tmp_q:
            if q[0] != i and tmp_q[-1] != i:
                break

    return answer

