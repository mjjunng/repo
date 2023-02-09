# sol 1) 단순 구현: 실패 + 시간초과

def check(lst):
    for i in lst:
        if i == 0:
            return False
    return True

def solution(n, stations, w):
    answer = 0
    
    dis = [0 for _ in range(n+1)]
    
    for i in range(len(stations)):
        dis[stations[i]] = 1
        
        for j in range(stations[i]+1, stations[i]+w+1):
            if stations[i]+w+1 > n+1:
                break
            dis[j] = 1
        for j in range(stations[i]-1, stations[i]-w-1, -1):
            if stations[i]-w < 0:
                break
            dis[j] = 1

    if check(dis):
        return 0
    cnt = 0

    for i in range(1, len(dis)):
        if dis[i] == 0:
            cnt += 1
        else:
            if cnt % (w * 2 + 1) == 0:
                answer += cnt // (w * 2 + 1)
            else:
                answer += cnt // (w * 2 + 1) + 1
            cnt = 0
    if cnt > 0:
        if cnt % (w * 2 + 1) == 0:
            answer += cnt // (w * 2 + 1)
        else:
            answer += cnt // (w * 2 + 1) + 1
        
    return answer

# sol 2) 모든 아파트 탐색하면서 전파 닿는지 안닿는지 확인 x -> 전파가 닿지 않는 구간의 길이 구함 
# 위 풀이에서 cnt가 결국 전파가 닿지 않는 구간의 길이임

def solution(n, stations, w):
    answer = 0
    dis = []    # 전파가 닿지 않는 구간의 길이 저장 

    for i in range(1, len(stations)):
        dis.append((stations[i]-w-1) - (stations[i-1]+w))

    
    # 첫 번째 아파트 ~ 첫 번째 기지국이 설치된 아파트 사이에서의 전파가 닿지 않는 구간의 길이 
    dis.append(stations[0]-w-1)
    
    # 마지막 기지국이 설치된 아파트 ~ 마지막 아파트 사이에서의 전파가 닿지 않는 구간의 길이 
    dis.append(n - (stations[-1]+w))
    
    for i in dis:
        if i <= 0:  # 전파가 닿지 않는 구간의 길이가 0이하면 고려X
            continue

        if i % (w * 2 + 1) == 0:
            answer += i // (w * 2 + 1)
        else:
            answer += i // (w * 2 + 1) + 1

        
    return answer
