# sol1) 효율성 실패

def solution(m, n, puddles):  
    board = [[0 for _ in range(m)] for _ in range(n)]
    board[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if [j+1, i+1] not in puddles:
                if 0 <= i-1:
                    board[i][j] += (board[i-1][j]) % 1000000007
                
                if 0 <= j-1:
                    board[i][j] += (board[i][j-1]) % 1000000007

    return board[n-1][m-1]
  
  
  # sol2)
  
  def solution(m, n, puddles):  
    board = [[0 for _ in range(m+1)] for _ in range(n+1)]
    board[1][1] = 1
    
    for x, y in puddles:
        board[y][x] = -1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
                
            if board[i][j] == -1:
                board[i][j] = 0
            else:
                board[i][j] = (board[i-1][j] + board[i][j-1]) % 1000000007

    return board[n][m]
