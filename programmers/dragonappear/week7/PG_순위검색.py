# https://school.programmers.co.kr/learn/courses/30/lessons/72412
from collections import defaultdict
from bisect import bisect_left


class Node:
    def __init__(self) -> None:
        self.scores = []
        self.child = defaultdict(Node)


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word.split():
            if ch.isalpha():
                node = node.child[ch]
            else:
                node.scores.append(int(ch))
                node.scores.sort()

    def search(self, node, arr) -> int:
        global cnt
        if len(arr) == 1:
            lt = bisect_left(node.scores, int(arr[0]))
            cnt += len(node.scores)-lt
            return

        a = arr.pop(0)
        if a != '-':
            node = node.child[a]
            self.search(node, arr)
        else:
            for n in node.child.values():
                self.search(n, arr[:])


cnt = 0


def solution(info, query):
    global cnt
    answer = []
    trie = Trie()

    for i in info:
        trie.insert(i)

    for que in query:
        cnt = 0
        q = [s for s in que.split(" ") if s != 'and']
        trie.search(trie.root, q)
        answer.append(cnt)
    return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
print(solution(info, query))
