# greedy

n, m = map(int, input().split())

if n == 1:
    print(1)
elif n == 2:
    print(min(4, (m+1)//2))
else:
    if m < 7:
        print(min(4, m))
    else:
        print(5 + m - 7)  # m이 7일 때 최대 칸: 5 + m-7
