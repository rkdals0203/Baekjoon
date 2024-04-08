v,e = map(int,input().split())
parent = [0]*(v+1)
for i in range(v+1):
  parent[i] = i

def find(node):
  if parent[node] != node:
    parent[node] = find(parent[node])
  return parent[node]

def union(node1, node2):
  a = find(node1)
  b = find(node2)
  if a == b:
    return
  elif a > b:
    parent[node1] = find(node2)
  else:
    parent[node2] = find(node1)

for _ in range(e):
  x,a,b = map(int,input().split())
  if x == 0:
    union(a,b)
  elif x == 1:
    parent_a = find(a)
    parent_b = find(b)
    if parent_a == parent_b:
      print("YES")
    else:
      print("NO")