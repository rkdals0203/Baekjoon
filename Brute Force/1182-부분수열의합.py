n, s = map(int,input().split())
arr = list(map(int,input().split()))
count = 0
add = 0
visited = [0]*n

def dfs(current):
  global count
  global add
  # 종료조건
  if add == s:
    count+=1
    return
  #순회
  for i in range(current,n):
    if visited[i]==0:
      visited[i]=1
      add += arr[i]
      dfs(current+1)
      visited[i]=0


dfs(0)
print(count)