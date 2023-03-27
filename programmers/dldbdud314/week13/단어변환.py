"""
** BFS 완전탐색
"""
from collections import deque


def valid(w1, w2):
    if len(w1) != len(w2):
        return False
    d_cnt = 0
    for c1, c2 in zip(w1, w2):
        if c1 != c2:
            d_cnt += 1
        if d_cnt > 1:
            return False
    return True


def solution(begin, target, words):
    queue = deque([(begin, 0)])  # 단어, 단계
    visited = [False] * len(words)
    while queue:
        word, step = queue.popleft()

        if word == target:
            return step

        for i in range(len(words)):
            if not visited[i] and valid(word, words[i]):
                visited[i] = True
                queue.append((words[i], step + 1))

    return 0
