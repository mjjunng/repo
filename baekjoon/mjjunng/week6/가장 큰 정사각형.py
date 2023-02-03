import sys


'''
    풀이 방법 1: 시간 초과 
    
    완전탐색하면서 1인 경우 길이를 1씩 증가시켜보면서 정사각형인지 확인 
'''

def check(start_y, start_x, end_y, end_x):

    for i in range(start_y, end_y+1):
        for j in range(start_x, end_x+1):
            if board[i][j] == 0:
                return False

    return True

if __name__ == "__main__":
    sys.stdin = open("input.txt", "rt")
    n, m = map(int, input().split())
    board = []
    ans = 0

    for _ in range(n):
        board.append(list(map(int, input())))

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                tmp = 1
                nj = j+1
                ni = i+1
                while nj < m and ni < n:
                    if board[ni][nj] == 0:
                        break

                    if not check(i, j, ni, nj):
                        break
                    nj += 1
                    ni += 1
                    tmp += 1

                if tmp > ans:
                    ans = tmp

    print(ans ** 2)
