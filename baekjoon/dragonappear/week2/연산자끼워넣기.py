# 연산자 끼워넣기 https://www.acmicpc.net/problem/14888
import sys
input = sys.stdin.readline


"""풀이
<DFS>

문제특징:
- 숫자 자리는 고정
- 숫자 사이에 들어가는 연산자만 순서변경하면서 계산

연산자에 대한 순열문제여서 DFS로 풀이

"""


# 재귀
def recursive(level:int,total:int)->None:
    global mx,mn

    # 종료
    if level == n:
        mx,mn= max(mx,total),min(mn,total) # 최댓값,최솟값 업데이트
        return 
    
    # 재귀 
    for op_type in range(OPERTATOR):
        if operators[op_type]>0:
            operators[op_type]-=1 # 방문 체크 표시
            next = calculate(total,numbers[level],op_type) # 사칙연산
            recursive(level+1,next) # 재귀
            operators[op_type]+=1 # 방문 체크 해제

# 사칙연산
def calculate(total:int,number:int,op_type:int)->int:
    if op_type==0:
        return total + number
    elif op_type==1:
        return total - number
    elif op_type==2:
        return total * number
    else:
        return int(total / number)

if __name__ == "__main__":
    # input
    n = int(input())
    numbers = list(map(int,input().split()))
    operators = list(map(int,input().split()))
    OPERTATOR = len(operators)

    # 초기화
    mx,mn = -sys.maxsize,sys.maxsize
    
    # 재귀
    recursive(1,numbers[0])

    # 출력
    print(mx,mn)