# https://www.acmicpc.net/problem/2629 양팔저울
import sys
input = sys.stdin.readline

"""풀이

문제특징:
- 주어진 모든 추를 모두 사용해야 하는 것은 아니다.

# 1. 부분집합(DFS)
- 양쪽으로 subset을 분할
- 양쪽마다 subset의 subset 구하기
-> 시간복잡도 너무 올라감

# 2. DP

- 조건으로 주어진 구슬을 저울에 추가해도 되고, 안해도 된다

조건식:
dp[level][weight] = True -> weight인 구슬을 추가 시 수평O
dp[level][weight] = False -> weight인 구슬을 weight 추가 시 수평X

조건식:
dp[level][weight]=
(dp[level-1][weight-beads[level-1]]) or # 같은쪽에 추가했을때
(dp[level-1][abs(weight-beads[level-1])]) or # 반대쪽에 추가했을때
(dp[level-1][weight-0]) # 추가안했을때


"""

def recursive(level:int,weight:int)->None:

    if(level>n) or (dp[level][weight]==True): return
    
    # 저울에 weight 올렸을 때 수평 O
    dp[level][weight] = True

    recursive(level+1,weight+beads[level]) # 추를 구슬 쪽에 올렸을 때 무게
    recursive(level+1,abs(weight-beads[level])) # 추를 구슬 반대편에 올렸을 때 무게
    recursive(level+1,weight) # 추를 안올림

if __name__ == "__main__":
    n = int(input().strip())
    beads =  list(map(int,input().split()))
    beads += [0] * (32-len(beads))
    m = int(input().strip())
    inputs = list(map(int,input().split()))

    # DP 테이블 초기화
    dp = [ ([False] * 40_001) for _ in range(32)]
    
    # DP 테이블 세팅
    recursive(0,0)

    # 추 추가
    results = []
    for i in inputs:
        if dp[n][i]==True:
            results.append("Y")
        else:
            results.append("N")
    
    print(*results)