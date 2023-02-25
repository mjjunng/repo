import sys
import heapq


if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    n = int(input())
    hq = []

    for _ in range(n):
        x = int(sys.stdin.readline())

        if x == 0:
            if len(hq) > 0:
                print(heapq.heappop(hq))
            else:
                print(0)
        else:
            heapq.heappush(hq, x)
