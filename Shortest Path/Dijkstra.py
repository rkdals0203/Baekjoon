import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드, 간선 개수 입력받기
n,m = map(int,input().split())
#시작노드 입력받기
start = int(input())
#연결 정보 graph 초기화
graph = [[] for _ in range(n+1)]
#Distance 초기화
distance = [INF]*(n+1)
#간선 개수만큼 비용정보 입력
for _ in range (m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))

#다익스트라 알고리즘 수행
def dijkstra(start):
  q=[]
  #시작노드로 가기위한 최단 경로는 0으로 설정해서 큐에 삽입
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    #최단거리가 짧은 노드 꺼내기
    dist,now = heapq.heappop(q)
    #꺼낸 최단 거리가 원래 있는 것 보다 길다면(이미 최단거리를 찾은 것) 무시
    if dist > distance[now]:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]: #현재 큐에서 뽑은 노드 거쳐서 가는게 원래 최단거리보다 짧다면
        distance[i[0]]=cost #최단거리 갱신
        heapq.heappush(q,(cost,i[0]))

#실행 및 프린트
dijkstra(start)
for i in range (1,n+1):
  if distance[i]==INF:
    print("INFINITY")
  else:
    print(distance[i])


#2
INF = int(1e9)
n,m = map(int,input().split())
start = int(input())

graph = [[]for _ in range(n+1)]
visited = [False]*(n+1)
distance = [INF]*(n+1)

for _ in range(m):
  a,b,c = map(int,input().split())
  graph[a].append((b,c))

def get_smallest_node():
  min_value = INF
  min_index = 0
  for i in range(n+1):
    if min_value>distance[i] and not visited[i]:
      min_value = distance[i]
      min_index = i
  return min_index

def dijkstra(start):
  #시작 노드 초기화
  distance[start] = 0
  visited[start] = True
  for i in graph[start]:
    distance[i[0]] = i[1]
  #나머지 노드
  for j in range(n-1): #n-1번 반복
    now = get_smallest_node()
    visited[now] = True
    for k in graph[now]:
      if distance[k[0]] > distance[now]+k[1]: #기존 최단경로보다 이 경로 통해서 가는게 더 빠르다면
        distance[k[0]] = distance[now]+k[1]

dijkstra(start)
print(distance)

import heapq

INF = int(1e9)
n,m = map(int,input().split())
start = int(input())

graph = [[]for _ in range(n+1)]
visited = [False]*(n+1)
distance = [INF]*(n+1)

for _ in range(m):
  a,b,c = map(int,input().split()) #a부터 b까지 가는 거리가 c라는 뜻
  graph[a].append((b,c))

def dijkstra(start):
  queue = []
  #시작 노드 초기화
  heapq.heappush(queue,(0,start))
  distance[start] = 0

  while queue:
    dist,now = heapq.heappop(queue)
    if visited[now] == True: #visited가 이미 참이면 무시
      continue
    visited[now] = True
    for i in graph[now]:
        if distance[i[0]] > distance[now]+i[1]: #기존 최단경로보다 이 경로 통해서 가는게 더 빠르다면
          distance[i[0]] = distance[now]+i[1]
          heapq.heappush(queue,(distance[i[0]],i[0]))

dijkstra(start)
print(distance)

