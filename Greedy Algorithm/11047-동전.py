n,k = map(int,input().split())
coins = [0]*n
count = 0
for i in range(n):
  coins[i] = int(input())

coins.sort(reverse=True)

for coin in coins:
  if coin<=k:
    count+=k//coin
    k=k%coin

print(count)