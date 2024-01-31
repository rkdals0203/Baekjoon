from sys import stdin
n = int(stdin.readline().strip())
dp=[0]*(n+1) #10이라는 숫자를 알고 싶으면, 0으로 11개 채우기 dp[0]~dp[10]
for i in range(2,n+1): #dp[0] = 안씀, dp[1] = 0
  dp[i] = dp[i-1]+1
  if i%2==0:
    dp[i] = min(dp[i],dp[i//2]+1)
  if i%3==0:
    dp[i] = min(dp[i],dp[i//3]+1)
print(dp[n])


x = int(input())

dp = [0]*(x+1)

dp[1]=0
dp[2]=1
for i in range (3, x+1):
  dp[i] = dp[i-1]+1
  if i%5==0:
    dp[i] = min(dp[i],dp[i//5]+1)
  if i%3==0:
    dp[i] = min(dp[i],dp[i//3]+1)
  if i%2==0:
    dp[i] = min(dp[i],dp[i//2]+1)

print(dp[x])