# 초기화 작업
v, e = map(int, input().split())
parent = [0] * (v + 1)
edges = []
result = 0
costs = []

for i in range(v + 1):
    parent[i] = i

# 비용에 따른 오름차순 정렬
for _ in range(e):
    node1, node2, cost = map(int, input().split())
    edges.append((cost, node1, node2))
edges.sort()

# 최소 신장 트리 -> 서로소 집합 자료구조이기 때문에 find와 union 구현
def find(node):
  if parent[node] != node:
      parent[node] = find(parent[node])
  return parent[node]

def union(node1, node2):
    root_node1, root_node2 = find(node1), find(node2)
    if root_node1 == root_node2:
        return
    if root_node1 < root_node2:
        parent[root_node2] = root_node1
    else:
        parent[root_node1] = root_node2

# 간선 추가 및 비용 계산
for edge in edges:
  cost, node1, node2 = edge
  if find(node1) != find(node2):
      union(node1, node2)
      costs.append(cost)

# 비용을 오름차순으로 정렬
costs.sort(reverse=True)

# 최소 신장 트리에 포함되는 간선의 비용 계산
for i in range(1, len(costs)):
    result += costs[i]

print(result)