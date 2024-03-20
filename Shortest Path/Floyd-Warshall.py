INF = int(1e9)

#노드 및 간선의 개수를 입력받기
n,m = map(int,input().split())

#2차원 리스트 만들고 초기화
graph = [[INF]*(n+1) for _ in range (n+1)] #[INF]*(n*1) == INF,INF,INF ... n+1개 == 한 행

#자기 자신에서 자기 자신으로 가는 비용은 0
for i in range (n+1):
  for j in range (n+1):
    if i == j:
      graph[i][j] = 0

#각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range (m):
  a,b,c = map(int,input().split()) #a==출발 b==도착 c==비용
  graph[a][b] = c

#점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range (1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

#수행된 경과 출력
for i in range (1,n+1):
  for j in range (1,n+1):
    if graph[i][j] == INF:
      print("INFINITY", end=" ")
    else:
      print(graph[i][j], end=" ")
  print()


#2
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
