from collections import deque

v,e = map(int,input().split())
indegree = [0]*(v+1) #진입차수 0으로 초기화
graph = [
  [] for _ in range (v+1)
]
result = []

for _ in range(e):
  a, b = map(int,input().split())
  graph[a].append(b)
  indegree[b] += 1

def topology_sort():
  queue = deque()
  for i in range(1,v+1):
    if indegree[i] == 0:
      queue.append(i)
      result.append(i)
  while queue:
    now = queue.popleft()
    result.append(now)
    for j in graph[now]:
      indegree[j] -= 1
      if indegree[j] == 0:
        queue.append(j)


topology_sort()
for i in range(1,v+1):
  print(result[i], end=" ")