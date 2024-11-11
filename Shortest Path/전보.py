import heapq

INF = int(1e9)
n,m,c = map(int,input().split())
distance = [INF for _ in range(n+1)]
visited = [False for _ in range(n+1)]
graph = [[]for _ in range(n+1)]

for _ in range(m):
  x,y,z = map(int,input().split())
  graph[x].append((y,z))

def dijkstra(start):
  queue = []
  #시작노드 처리
  distance[start] = 0
  heapq.heappush(queue,(0,start))
  #시작노드와 연결된 노드부터 시작
  while queue:
    dist, node = heapq.heappop(queue) #우선수위 큐로, 자동적으로 가까운 노드부터 뽑음
    if dist > distance[node]: #경유하는 거리가 최단거리보다 길면 자동으로 거름
      continue
    visited[node] =True
    for i in graph[node]:
      cost = distance[node] + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(queue,(dist,node))

count = 0
result = []
dijkstra(c)
for j in distance:
  if j != 0 and j < INF: #0은 시작 노드, INF는 닿을 수 없는 노드
    count += 1
    result.append(j)
print(count,max(result))