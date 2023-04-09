import heapq
def solution(scoville, K):
    answer = 0
    if len(scoville) < 2:
        return -1
    
    if min(scoville) >= K:
        return 0

    heapq.heapify(scoville)
    
    while True:
        if len(scoville) == 1:
            if scoville[0] < K:
                return -1
            else:
                return answer
    
        fir_scoville = heapq.heappop(scoville)
        if fir_scoville >= K:
            return answer
        
        sec_scoville = heapq.heappop(scoville)
        heapq.heappush(scoville, fir_scoville + (sec_scoville * 2))
        answer += 1

    return answer
