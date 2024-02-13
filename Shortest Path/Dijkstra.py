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