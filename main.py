INF = int(1e9)
n,m = map(int,input().split())

graph = [
  [INF]*(n+1) for _ in range(n+1)
]

for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a][b] = c

# 생각 못한 부분
for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j:
      graph[i][j] = 0

for i in range (1,n+1): #step
  for j in range(1,n+1): #열
    for k in range(1,n+1): #행
      graph[j][k] = min(graph[j][k],(graph[j][i]+graph[i][k]))

for i in range(1,n+1):
  for j in range(1,n+1):
    print(graph[i][j], end=" ")
  print("")
    