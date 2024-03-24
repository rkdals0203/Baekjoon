INF = int(1e9)
n, m = map(int,input().split())

#그래프 초기화
graph = [[INF]*(n+1) for _ in range (n+1)]
for i in range (1,n+1):
  for j in range(1,n+1):
    if i == j:
      graph[i][j]=0

#이동 가능정보
for _ in range (m):
  start, end = map(int,input().split())
  graph[start][end] = 1
  graph[end][start] = 1

x, k = map(int,input().split())

#플로이드 워셜 알고리즘 수행
for z in range (1, n+1):
  for i in range (1, n+1):
    for j in range (1, n+1):
      graph[i][j] = min(graph[i][j],(graph[i][z]+graph[z][j]))

#출력
if graph[1][k]+graph[k][x] >= INF:
    print(-1)
else:
  print(graph[1][k]+graph[k][x])


#2
INF = int(1e9)
n,m = map(int,input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range (1,n+1):
  graph[i][i] = 0
for _ in range(m):
  a,b =map(int,input().split())
  graph[a][b]=1
  graph[b][a]=1

x,k = map(int,input().split())
for i in range(1,n+1):
  for j in range(1,n+1):
    for k in range(1,n+1):
      graph[j][k] = min(graph[j][k],(graph[j][i]+graph[i][k]))


if graph[1][k]+graph[k][x] >= INF:
  print(-1)
else:
  print(graph[1][k]+graph[k][x])