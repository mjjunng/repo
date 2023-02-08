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
