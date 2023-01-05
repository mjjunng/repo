'''
BRUTEFORCE: O(n^2)

1. 주어진 연산자 개수대로 연산자 리스트 생성 -> operators
2. 연산자 리스트 순열 돌면서(set으로 중복제거) 연산, 최대값/최소값 갱신
'''
from itertools import permutations

OPS = ('+', '-', '*', '/')


# 연산 메소드
def calc(op1, op2, opr):
    if opr == OPS[0]:
        return op1 + op2
    if opr == OPS[1]:
        return op1 - op2
    if opr == OPS[2]:
        return op1 * op2
    if opr == OPS[3]:
        return op1 // op2 if op1 > 0 else -(-op1 // op2)


n = int(input())
numbers = list(map(int, input().split()))
operators_count = list(map(int, input().split()))

# 연산자 개수만큼 생성
operators = []
for i in range(len(operators_count)):
    operators.extend(OPS[i] * operators_count[i])

# 계산하면서 갱신하기
largest, smallest = -float('inf'), float('inf')
for x in set(permutations(operators)):
    cur_operators = list(x)
    num = numbers[0]
    for i in range(1, len(numbers)):
        num = calc(num, numbers[i], cur_operators[i-1])
    smallest = min(smallest, num)
    largest = max(largest, num)

print(largest)
print(smallest)