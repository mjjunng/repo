# https://school.programmers.co.kr/learn/courses/30/lessons/142085
from collections import deque
import heapq as hq

# 우선순위큐 
# O(nlogn)
def solution(n,k,enemy):

    # 예외처리
    if n > sum(enemy):
        return len(enemy)

    answer = 0
    enemies = deque(enemy)
    heapq = []
    
    # 게임 진행
    while n>=0 and enemies:
        enemy_number = enemies.popleft()
        n -= enemy_number
        hq.heappush(heapq,-enemy_number) # 적수 카운팅 -> 최대힙 구성

        if n>=0: answer+=1
        elif k>0: # 게임에서 질 경우, 진행했었던 게임들중 적의수가 가장 많았던 단계에서 무적권 사용
            n-=hq.heappop(heapq)
            k-=1
            answer += 1
        
    return answer