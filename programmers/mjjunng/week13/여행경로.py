# sol1) implementation - 실패

def solution(tickets):
    answer = []
    start = 'ICN'
    answer.append(start)
    visited = []
    
    while len(answer) <= len(tickets):
        nxt_start = 'ZZZ'
        idx = 0
        for i, lst in enumerate(tickets):
            s = lst[0]
            e = lst[1]
            if s == start:
                if e < nxt_start and [start, e, i] not in visited:
                    nxt_start = e
                    idx = i
                    
        visited.append([start, nxt_start, idx])
        start = nxt_start
        answer.append(start)

    return answer
