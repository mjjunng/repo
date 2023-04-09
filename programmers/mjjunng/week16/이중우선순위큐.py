import heapq

def solution(operations):
    answer = []
    hq = []

    for order in operations:
        lst = order.split(" ")
        if lst[0] == 'I':
            heapq.heappush(hq, int(lst[1]))
        else:
            if int(lst[1]) < 0:
                if hq:
                    hq.pop(0)
            else:
                if hq:
                    hq.pop()        
    if hq:
        answer.append(max(hq))
        answer.append(min(hq))
    else:
        answer.extend([0, 0])
        
    return answer
