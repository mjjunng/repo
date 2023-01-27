# https://school.programmers.co.kr/learn/courses/30/lessons/148653

# 재귀
def solution(storey):
    # Base Condition
    if storey<10: return storey if storey <= 5 else 10-storey+1
    one,ten = storey % 10,(storey // 10) % 10 # 1의 자리,10의 자리
    if one>5: 
        return (10-one) + solution((storey+10)//10)
    elif one==5: 
        return 5 + solution( ((storey+10)//10) if ten>=5 else (storey//10))
    else: 
        return one + solution(storey//10)

print(solution(2554))

# 반복
def solution_iterative(storey):
    answer = 0 # 마법의 돌
    while storey:
        one,ten = storey % 10,(storey // 10) % 10 # 1의 자리,10의 자리  
        if one>5:
            answer+=10-one
            storey+=10
        elif one==5:
            answer+=5
            storey+= 10 if ten>=5 else 0
        else:
            answer+=one
        storey//=10
    return answer

print(solution_iterative(2554))

"""
Idea
일의 자리 처리 + 나누기 10 반복

1. 일의 자리
    - 일의 자리 > 5 :  올림
    - 일의 자리 == 5 : 십의 자리 숫자가 5 이상일 경우 올림, 5 미만일 경우 내림
    - 일의 자리 < 5: 내림
2. storey를 10으로 나누고 1~3번 과정을 storey가 0이 될 때까지 반복
3. 2번 과정을 거치면서 사용한 마법의 돌의 개수를 반환
"""
