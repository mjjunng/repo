'''
    첫 번째 풀이 방법: 완전 탐색
    상태 트리를 통해 매 라운드마다 무적권을 쓸 지 안 쓸지 가지쳐서 모든 경우의 수 탐색하는 방법
    -> 시간 초과 & 실패 & 런타임 에러 발생
'''

answer = 0

def dfs(lev, n, k, enemy):
    global answer

    if lev > len(enemy) - 1:
        return

    if n < 0:
        if answer < lev - 1:
            answer = lev - 1
        return

    if k > 0:
        dfs(lev + 1, n, k - 1, enemy)  # 무적권 사용
    dfs(lev + 1, n - enemy[lev], k, enemy)  # 무적권 사용X

def solution(n, k, enemy):
    if len(enemy) <= k:
        return len(enemy)

    dfs(0, n, k, enemy)
    return answer


'''
    두 번째 풀이 방법: heapq 
    완전 탐색이 아닌 다른 방법 모색 
    -> 적의 수가 큰 상위 n개 는 무적권 사용해야 함 
    -> 문제 1단계부터 차례대로 라운드를 진행함과 동시에 상위 n개를 뽑을 수 없음 
    -> heapq로 문제 해결 
    
    일단 우선순위 큐에 적의 수 집어 넣은 다음, 무적권의 개수를 초과한다면 가장 적은 적의 수로 방어함  
'''
import heapq

def solution(n, k, enemy):
    h = []  # 무적권으로 방어할 라운드의 적의 수 저장

    for i in range(len(enemy)):
        heapq.heappush(h, enemy[i])

        # 무적권의 수보다 방어할 라운드가 많은 경우
        # 적의 수가 가장 작은 라운드 병력 감소
        if len(h) > k:
            n -= heapq.heappop(h)

        # 병력이 0 보다 작아질 때 게임 종료
        if n < 0:
            return i

    return len(enemy)
