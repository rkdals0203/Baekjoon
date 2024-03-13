n, m = map(int, input().split())
coins = []
for _ in range(n):
  coins.append(int(input()))
dp = [10001] * (m + 1)
dp[0] = 0

for j in range(m + 1):
  for coin in coins:
    if j-coin >= 0:
        dp[j] = min(dp[j], dp[j - coin] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])