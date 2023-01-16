# 첫 번째 풀이 방법: end_idx를 줄여나가는 방식 -> 시간초과 

def solution(cap, n, deliveries, pickups):
    answer = 0
    end_idx = n-1   # 배달해야 할 맨 끝 집의 인덱스
    
    while end_idx > -1:
        # 배달 
        # 물류 창고에서 최대로 택배를 가져와서 맨 끝 집부터 배달함
        cur = cap # 현재 트럭에 실린 택배의 수 
        for i in range(end_idx, -1, -1):
            if deliveries[i] > cur:
                deliveries[i] -= cur
                cur = 0 # 더이상 배달할 택배가 없으므로 break
                break
            else:
                cur -= deliveries[i]
                deliveries[i] = 0
              
        # 수거
        # 맨 끝 집부터 가져올 수 있는 최대의 수거 박스를 가져옴
        end = 0  # 트럭에 실린 박스의 개수 
        for i in range(end_idx, -1, -1):
            store = cap - end   # 트럭에 실을 수 있는 박스의 개수
            if store > pickups[i]:
                end += pickups[i]
                pickups[i] = 0
            else:
                pickups[i] -= store
                end = cap   # 더이상 박스를 실을 수 없으므로 break
                break
        
        # 배달하거나 수거할 택배가 있을 때 왕복 거리 더함 
        if cur != cap or end != 0:
            answer += (end_idx + 1) * 2 
        else:
            break
        
        # 배달과 수거를 완료했다면, 맨 끝 집을 그 앞 집으로 갱신 
        for i in range(end_idx, -1, -1):
            if deliveries[i] == 0 and pickups[i] == 0:
                end_idx -= 1
            else:
                break
        
    return answer
  
  # 두 번째 풀이 방법: stack
  def solution(cap, n, deliveries, pickups):
    answer = 0
    d = []
    p = []
    for i in range(n):
        if deliveries[i] > 0:
            d.append([i, deliveries[i]])
        if pickups[i] > 0:
            p.append([i, pickups[i]])
    
    while d or p:
        # 배달 
        # 물류 창고에서 최대로 택배를 가져와서 맨 끝 집부터 배달함
        max_len = -1
        delivered = 0
        while delivered < cap and d:
            now = d.pop()
            if cap < delivered+now[1]:
                d.append([now[0], delivered+now[1]-cap])
                delivered = cap

            else:
                delivered += now[1]
            max_len = max(max_len, now[0])
        # 수거
        # 맨 끝 집부터 가져올 수 있는 최대의 수거 박스를 가져옴
        picked = 0  
        while picked < cap and p:
            now = p.pop()
            if cap < now[1]+picked:
                p.append([now[0], now[1]+picked-cap])
                picked = cap   # 더이상 박스를 실을 수 없으므로 break

            else:
                picked += now[1]
            max_len = max(max_len, now[0])
        
        # 배달하거나 수거할 택배가 있을 때 왕복 거리 더함 
        if max_len == -1:
            break
        answer += (max_len + 1) * 2 
       

    return answer
