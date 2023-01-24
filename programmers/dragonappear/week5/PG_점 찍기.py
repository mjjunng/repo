# https://school.programmers.co.kr/learn/courses/30/lessons/140107
from math import floor,sqrt

# 원그려서 풀이
def solution(k, d):
    ans=0
    for i in range(0,d+1,k):
        x = floor(sqrt(d**2-i**2))
        ans += int(x//k)+1
    return ans

# 브루트 포스
# 시간초과
def solution_1(k, d):
    return sum( 1 for i in range(0,d+1,k) for j in range(0,d+1,k) if i**2+j**2<=d**2)

print(solution(2,4))
print(solution(1,5))