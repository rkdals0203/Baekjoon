v,e = map(int,input().split())
parent = [0]*(v+1)
# 개선 전
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
    return find(parent[node])
  else:
    return node

for _ in range(e):
  a,b = map(int,input().split())
  union(a,b)

print("각 원소가 속한 집합: ", end=" ")
for i in range(1,v+1):
  print(find(i), end=" ")

print("")

print("각 원소의 직계 부모: ", end=" ")
for j in range(1,v+1):
  print(parent[j], end=" ")

# 개선 후(경로압축)
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
  union(a,b)

print("각 원소가 속한 집합: ", end=" ")
for i in range(1,v+1):
  print(find(i), end=" ")

print("")

print("각 원소의 직계 부모: ", end=" ")
for j in range(1,v+1):
  print(parent[j], end=" ")