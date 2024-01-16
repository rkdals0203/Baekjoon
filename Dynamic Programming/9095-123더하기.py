from sys import stdin
t = int(stdin.readline().strip())

for z in range(t):
  n = int(stdin.readline().strip())
  dp=[0]*(n+3) #10이라는 숫자를 알고 싶으면, 0으로 11개 채우기 
  dp[0]=1
  dp[1]=1
  for i in range(2,n+3): #dp[0] = 1, dp[1] = 1
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
  print(dp[n])

