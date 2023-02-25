# 완전 탐색 O(n^2)

def play(idx, n, visited, cards):
    res = 0
    
    while visited[idx] != 1:  # 이전에 선택하지 않은 상자이면
        visited[idx] = 1    # 선택 
        res += 1    # 상자 개수 +1
        idx = cards[idx] - 1    # 다음 선택할 상자의 인덱스 갱신 
    
    return res

def solution(cards):
    answer = 0
    n = len(cards)
    
    for i in range(n):
        visited = [0 for _ in range(n)]
        score1 = play(i, n, visited, cards) # 1번 상자 
        
        for j in range(n):
            if visited[j] == 0:
                score2 = play(j, n, visited, cards) # 2번 상자 
                
                if score1 * score2 > answer:    # 모든 케이스 탐색해서 최댓값 갱신 
                    answer = score1 * score2
        
    return answer
