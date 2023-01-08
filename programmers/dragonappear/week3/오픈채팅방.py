# https://school.programmers.co.kr/learn/courses/30/lessons/42888
from typing import List
from collections import deque,defaultdict

# 해시테이블을 활용한 풀이
# 시간복잡도: O(n), n is the number of records
# 시간복잡도: O(n), n is the number of records 
def solution(record:List) -> List:
    answer = []

    trace = []
    uid_nickname_mapping = defaultdict(str)
    in_out_mapping = {"IN":"님이 들어왔습니다.","OUT":"님이 나갔습니다."}

    # O(n)
    for r in record:
        cmd = r.split()
        
        if len(cmd)>2:
            cmd_type,uid,nickname = cmd[0],cmd[1],cmd[2]
        else:
            cmd_type,uid = cmd[0],cmd[1]
        # O(1)
        if cmd_type == "Enter":
            uid_nickname_mapping[uid] = nickname
            trace.append([uid,"IN"])
        elif cmd_type == "Leave":
            trace.append([uid,"OUT"])
        else:
            uid_nickname_mapping[uid] = nickname
    
    # O(n)
    for t in trace:
        answer.append(uid_nickname_mapping[t[0]] + in_out_mapping[t[1]])

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))