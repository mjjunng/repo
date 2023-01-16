def find_max(a, n):
    ans = 0
    r = len(a)
    if r == n:
        return 1
    for c in range(n):
        if c in a:
            go = False
        else:
            go = True
            for p in range(r):
                for j in range(1, n):
                    if r < p+j:
                        break
                    if r == p+j:
                        if c == a[p]+j or c == a[p]-j:
                            go = False
                            break
        if go:
            ans += find_max(a+[c], n)
    return ans


def solution(n):
    return find_max([], n)