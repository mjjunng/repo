from queue import PriorityQueue


def solution(n, k, enemy):
    ans = 0
    pqueue = PriorityQueue()
    for i in range(len(enemy)):
        pqueue.put(enemy[i])
        if pqueue.qsize() > k:
            n -= pqueue.get()
        if n < 0:
            return i
        ans = i + 1
    return ans