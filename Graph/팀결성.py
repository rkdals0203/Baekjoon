v, e = map(int, input().split())
parent = [0] * (v + 1)
for i in range(v + 1):
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
  x, a, b = map(int, input().split())
  if x == 0:
    union(a, b)
  elif x == 1:
    parent_a = find(a)
    parent_b = find(b)
    if parent_a == parent_b:
      print("YES")
    else:
      print("NO")

#2
#초기화
n, m = map(int, input().split())
parent = [0] * (n + 1)
for i in range(n + 1):
  parent[i] = i


def find(node):
  if parent[node] != node:
    parent[node] = find(parent[node])
  return parent[node]


def union(node1, node2):
  root_node1, root_node2 = find(node1), find(node2)
  if root_node1 == root_node2:
    return
  elif root_node1 > root_node2:
    parent[node1] = root_node2
  else:
    parent[node2] = root_node1


#명령 실행
for _ in range(m):
  x, a, b = map(int, input().split())
  if x == 0:
    union(a, b)
  elif x == 1:
    root_a, root_b = find(a), find(b)
    if root_a == root_b:
      print("Yes")
    else:
      print("No")
