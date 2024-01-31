n = int(input())
arr = list(map(int,input().split()))

dp = [0]*(n) #n이 4라면 0~3까지
dp[0] = arr[0]
dp[1] = arr[1]
dp[2] = dp[0] + arr[2]

for i in range (3, n): #3~3까지
  dp[i] = max(dp[i-2],dp[i-3]) + arr[i]

print(max(dp))
