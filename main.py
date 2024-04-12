from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
cost = [0]*(n+1)
result = [0]*(n+1)

for i in range(1,n+1):
  temp = list(map(int,input().split()))
  cost[i] = temp[0]
  result[i] = temp[0]
  coming = temp[1:-1]
  indegree[i] = len(coming)
  for j in coming:
    graph[j].append(i)

print(indegree)
print(graph)

def topology_sort():
  queue = deque()
  #진입차수 0인 것 큐에 넣기, 얘네들은 result가 cost와 같으므로 신경쓸 필요 x
  for i in range(1,n+1):
    if indegree[i] ==0:
      queue.append(i)
  while queue:
    now = queue.popleft()
    for j in graph[now]:
      result[j] = max(result[j],result[now]+cost[j])
      indegree[j]-=1
      if indegree[j]==0:
        queue.append(j)
    
    
  
  
  