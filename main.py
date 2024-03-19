import heapq
INF = int(1e9)
n,m = map(int,input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
distance = [INF]*(n+1)

for _ in range(m):
  a,b,c = map(int,input().split()) #a부터 b까지 거리가 c이다
  graph[a].append((b,c))

def dijkstra(start):
  queue = []
  #시작 노드 처리
  heapq.heappush(queue,(0,start))
  visited[start] = True
  distance[start] = 0
  #나머지 노드
  while queue:
    dist, now = heapq.heappop(queue)
    if dist > distance[now] and not visited[now]: #지금 원소의 거리보다 원래 최단거리가 더 짧으면 Pass
      continue
    for j in graph[now]:
      if distance[j[0]] > dist + j[1]: #j[0]이 노드, j[1]이 거리
        distance[j[0]] = dist + j[1]
        heapq.heappush(queue,(distance[j[0]],j[0]))

dijkstra(start)
print(distance)
  