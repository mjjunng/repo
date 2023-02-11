# implementation

import sys
from collections import Counter

if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    r1, c1, k = map(int, input().split())
    sec = 0
    board = []
    for _ in range(3):
        board.append(list(map(int, input().split())))

    while True:
        if r1-1 < len(board) and c1-1 < len(board[0]):  # index error 해결
            if board[r1-1][c1-1] == k:
                print(sec)
                break

        if 100 < sec:
            print(-1)
            break

        n = len(board)
        m = len(board[0])
        new = []    # R 또는 C연산을 한 결과

        if m <= n:  # R연산
            max_len = 0
            for i in board:
                c = Counter(i)
                c = sorted(c.items(), key=lambda x:(x[1], x[0]))
                row = []
                for a, b in c:
                    if a != 0:
                        row.append(a)
                        row.append(b)
                if len(row) > max_len:  # 나머지 부분 0으로 채우기 위해 가장 길이가 긴 행의 길이 저장
                    max_len = len(row)
                new.append(row)

            # 나머지 부분 0으로 채워서 모든 배열의 길이 맞춤
            for i in new:
                if len(i) < max_len:
                    for _ in range(max_len-len(i)):
                        i.append(0)

            # 행의 길이가 100을 넘어가는 경우, 나머지 버림 
            if len(new) > 100:
                new = new[:100]

        else:
            max_len = 0
            for j in range(len(board[0])):
                col = []    # 행 돌면서, 열에 해당하는 수 저장 
                t_col = []

                for i in range(len(board)):
                    if board[i][j] != 0:
                        col.append(board[i][j])

                c = Counter(col)
                c = sorted(c.items(), key=lambda x:(x[1], x[0]))

                for a, b in c:
                    t_col.append(a)
                    t_col.append(b)

                if len(t_col) > max_len:
                    max_len = len(t_col)
                new.append(t_col)

            for i in new:
                if len(i) < max_len:
                    for _ in range(max_len - len(i)):
                        i.append(0)

            new = list(zip(*new))   # 행과 열 바꾸기

            if len(new) > 100:
                new = new[:100]
        board = new[:]

        sec += 1
