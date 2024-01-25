n,m = map(int,input().split())

graph= []

for _ in range (n):
  row = list(map(int,input()))
  graph.append(row)
print(graph)

def dfs(y,x):
  if x<0 or y<0 or x>=m or y>=m:
    return False
  if graph[y][x]==0:
    graph[y][x]=1
    dfs(y-1,x)
    dfs(y+1,x)
    dfs(y,x-1)
    dfs(y,x+1)
    return True
  else:
    return False

ans = 0

for i in range (n):
  for j in range (m):
    if dfs(i,j) == True:
      ans+=1
print(ans)

