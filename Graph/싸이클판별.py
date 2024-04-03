cycle = False
v,e = map(int,input().split())
parent = [0]*(v+1)
for i in range(len(parent)):
  parent[i] = i

def union(node1, node2):
  if parent[node1] == parent[node2]:
    return
  if parent[node1] > parent[node2]:
    parent[node1] = parent[node2]
  else:
    parent[node2] = parent[node1]

def find(node):
  if parent[node] != node:
   parent[node] = find(parent[node])
  return parent[node]

for _ in range(e):
  a,b = map(int,input().split())
  if find(a) == find(b):
    cycle = True
    break
  else:
    union(a,b)

print(cycle)