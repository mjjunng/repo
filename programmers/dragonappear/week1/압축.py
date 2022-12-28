# https://school.programmers.co.kr/learn/courses/30/lessons/17684
from typing import List


# O(KN) 
# k = [1,N]
# N = length of str
def solution(msg:str)->List:
    answer = []
        
    # 예외 처리
    if not str:
        return answer

    # 사전 초기화
    letter_dict = {}
    for i in range(1,27):
        letter_dict[chr(i+64)] = i
    index = 27

    left = 0 # 왼쪽 포인터 초기화
    right = left + 1 # 오른쪽 포인터 초기화
    
    while left < len(msg):
        
        # 사전에 존재하지 않는 문자열까지 찾기
        while right<len(msg) and msg[left:right+1] in letter_dict:
            right += 1

        # 사전에 존재하지 않는 문자열까지 찾은 경우 -> 사전에 등록
        if  right<len(msg) and msg[left:right+1] not in letter_dict:
            letter_dict[msg[left:right+1]] = index
            index += 1
            
        # 단어 출력
        answer.append(letter_dict[msg[left:right]])

        # 포인터 업데이트
        left += right - left
        right = left +1
        
    return answer
            

print(solution("KAKAO"))
