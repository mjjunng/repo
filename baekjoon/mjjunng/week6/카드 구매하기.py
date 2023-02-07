'''
    풀이 방법: dp
    시간 복잡도: O(n**2)
'''

n = int(input())
cards = list(map(int, input().split()))
cards.insert(0, 0)
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    dp[i] = cards[i]
    for j in range(1, i):
        dp[i] = max(dp[i], dp[i-j] + cards[j])

print(dp[n])
