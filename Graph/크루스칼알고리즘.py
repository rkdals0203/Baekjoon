v,e = map(int,input().split())
parent = [0]*(v+1)
edges = [] #간선과 그 비용 정보를 담은 배열 생성
result = []
minimum_cost = 0

for i in range(len(parent)):
  parent[i] = i

def union(node1, node2):
  a = find(node1)
  b = find(node2)
  if a>b:
    parent[a] = b
  else:
    parent[b] = a

def find(node):
  if parent[node] != node:
    parent[node] = find(parent[node])
  return parent[node]

for _ in range(e):
  node1,node2,cost = map(int,input().split())
  edges.append((cost,node1,node2))
edges.sort()

for edge in edges:
  cost,node1,node2 = edge
  if find(node1) == find(node2):
    continue
  else:
    minimum_cost += cost
    result.append(edge)
    union(node1,node2)

print(minimum_cost)
print(result)