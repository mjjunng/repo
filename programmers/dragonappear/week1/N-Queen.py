# https://school.programmers.co.kr/learn/courses/30/lessons/12952

# dfs
# O(n^2)
def solution(n:int)->int:

    def is_possible_nqueen(cur_row:int)->bool:
        # 이전 행과 열이 같은지, 대각선인지 체크
        for prev_row in range(cur_row):
            if (table[prev_row] == table[cur_row]) or (cur_row-prev_row == abs(table[prev_row]-table[cur_row])):
                return False
        return True

    def nqueen(row:int)->None:
        global answer
            
        # 종료점 -> 행끝까지 도달한 경우 카운트
        if row==n:
            answer += 1
            return

        # 현재 행의 각 열에 퀸 두는 작업
        for i in range(n):
            table[row]=i
            if(is_possible_nqueen(row)):
                nqueen(row+1)

    table = [None]*n # i,k=col,row
    nqueen(0)
    return answer

answer = 0
print(solution(4))