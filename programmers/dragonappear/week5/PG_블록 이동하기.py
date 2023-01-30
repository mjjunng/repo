# https://school.programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque
def solution(board):
    
    # check out of board
    def OOB(r,c): return not(0<=r<N) or not(0<=c<N)
    
    # 현재 좌표에서 이동가능한 좌표 리턴
    def move(p1,p2):
            
        ret=[]
        # 좌우상하
        for dr,dc in dr_dc:
            if OOB(p1[0]+dr,p1[1]+dc) or OOB(p2[0]+dr,p2[1]+dc): continue
            if board[p1[0]+dr][p1[1]+dc]==0 and board[p2[0]+dr][p2[1]+dc]==0:
                ret.append(((p1[0]+dr,p1[1]+dc),(p2[0]+dr,p2[1]+dc)))
        
        # 가로에서 회전
        if p1[0]==p2[0]:
            for ro in rotate:
                if OOB(p1[0]+ro,p1[1]) or OOB(p2[0]+ro,p2[1]): continue
                if board[p1[0]+ro][p1[1]]==0 and board[p2[0]+ro][p2[1]]==0:
                    ret.append(((p1[0],p1[1]),(p1[0]+ro,p1[1]))) 
                    ret.append(((p2[0]+ro,p2[1]),(p2[0],p2[1]))) 
        # 세로에서 회전
        elif p1[1]==p2[1]:
            for ro in rotate:
                if OOB(p1[0],p1[1]+ro) or OOB(p2[0],p2[1]+ro): continue
                if board[p1[0]][p1[1]+ro]==0 and board[p2[0]][p2[1]+ro]==0:
                    ret.append(((p1[0],p1[1]),(p1[0],p1[1]+ro))) 
                    ret.append(((p2[0],p2[1]+ro),(p2[0],p2[1])))
        return ret
        
        
    N=len(board)
    dr_dc=[(0,1),(0,-1),(1,0),(-1,0)]
    rotate=[1,-1]
    q=deque([ ((0,0),(0,1),0) ])
    visit=set(((0,0),(0,1)))
    
    while q:
        p1,p2,dist=q.popleft()
        for mov in move(p1,p2):
            if (N-1,N-1) in mov: return dist+1
            if mov not in visit:
                q.append(tuple(list(mov)+[dist+1]))
                visit.add(mov)
                
print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
