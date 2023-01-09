# https://school.programmers.co.kr/learn/courses/30/lessons/92343
from typing import List
from collections import defaultdict
import sys
# DFS 완전탐색
mx = -sys.maxsize
def solution(info, edges):

    def dfs(cur_node:int,sheep_count:int,wolf_count:int,visitable:List,visited:List)->None:
        global mx

        if visited[cur_node]: return # 현재 노드를 방문한 경우 return
        else: visited[cur_node] = True # 현재 노드 방문 기록

        if info[cur_node]: # 현재 노드 == 늑대
            wolf_count += 1 # 늑대 카운트
            if wolf_count >= sheep_count: 
                return
        else: # 현재 노드 == 양
            sheep_count += 1 # 양 카운트
            mx = max(mx,sheep_count) # 양 마리 업데이트

        visitable.extend(binary_tree[cur_node]) 

        for next in visitable:
            dfs(next,sheep_count,wolf_count, [ n for n in visitable if n != next and not visited[n]],visited[:])
        
        
    visited = [False] * len(info) # 노드 방문 체크 변수 초기화
    binary_tree = defaultdict(list) # 트리 변수
    for src,dst in edges: # 트리 초기화
        binary_tree[src].append(dst)

    # dfs
    dfs(0,0,0,[],visited) # root node index , sheep_count, wolf_count , next_nodes , visited

    return mx