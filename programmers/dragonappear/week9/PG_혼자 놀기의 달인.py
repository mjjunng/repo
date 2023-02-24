# https://school.programmers.co.kr/learn/courses/30/lessons/131130
def solution(cards):

    def solve(st, box):
        while not vis[cards[st]]:
            vis[cards[st]] = True
            box.add(cards[st]-1)
            st = cards[st]-1

    def init():
        for e in box2:
            vis[e+1] = False

    N = len(cards)
    mx = -1

    for i in range(N):
        vis = [False]*(N+1)
        box1 = set()
        solve(i, box1)
        one, two = len(box1), 0

        for j in range(N):
            if vis[cards[j]]:
                continue

            box2 = set()
            solve(j, box2)
            two = max(two, len(box2))
            init()

        mx = max(mx, one*two)

    return mx


print(solution([8, 6, 3, 7, 2, 5, 1, 4]))
print(solution([2, 3, 1]))
