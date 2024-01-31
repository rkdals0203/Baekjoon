n,m = map(int,input().split())
moneys = []
for _ in range (n):
  moneys.append(int(input()))

dp = [0]*(max(max(moneys),m)+1)

for i in moneys:
  dp[i]=1

for i in range (len(dp)): #dp 테이블 순회
  for j in moneys:
    if i-j>0 and dp[i-j] !=0:
      dp[i] = dp[i-j]+1


if dp[m] == 0:
  print(-1)
else:
  print(dp[m])