# https://school.programmers.co.kr/learn/courses/30/lessons/92342
def solution(n, info):
    
    # dfs
    def dfs_score(depth,cnt,scores):
        if cnt==n:
            if depth<len(info):scores+=[0]*(11-depth)
            ret.add(tuple(scores))
            return
        
        if depth==len(info):
            if cnt<n: scores[depth-1]+=(n-cnt)
            ret.add(tuple(scores))
            return
        
        if cnt+info[depth]+1<=n: 
            dfs_score(depth+1,cnt+info[depth]+1,scores+[info[depth]+1])
        dfs_score(depth+1,cnt,scores+[0])
    
    # 아파치,라이언 차이 비교
    def calculate(lion):
        score_a,score_l=0,0
        for i in range(11):
            if (info[i] == 0 and lion[i]== 0) or i==10: continue
            elif info[i]>=lion[i]: score_a += (10-i)
            else: score_l += (10-i)
        if score_a>=score_l: return 0
        else: return (score_l-score_a)
    
    # 정렬
    def check(old,new):
        for i in range(10,-1,-1):
            if new[i]==old[i]: continue
            elif new[i]>old[i]: return new
            else: return old

    ret = set()
    dfs_score(0,0,[])
        
    mx=float('-inf')
    answer=[float('inf')]*11
    
    for lion in list(ret):
        rst = calculate(list(lion))
        if rst and rst>mx:
            mx=rst
            answer=lion
        elif rst and rst==mx:
            answer=check(answer,lion)
    
    if answer==[float('inf')]*11: 
        return [-1]        
    else:
        return list(answer)

print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1,[1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10,[0,0,0,0,0,0,0,0,3,4,3]))