import math

def solution(n, stations, w):
    # 첫 기지국 전에 기지 설치
    cnt = math.ceil((stations[0] - w - 1) / (w*2+1))
    # 첫 번째, 마지막 기지국 사이 기지 설치
    for i in range(len(stations)-1):
        d = stations[i+1] - stations[i]-2*w-1
        cnt += math.ceil(d / (w*2+1))
    # 마지막 기지국 뒤에 기지 설치
    cnt += math.ceil((n - stations[len(stations)-1] - w) / (w*2+1))
    return cnt

# 시간 복잡도: O(N)