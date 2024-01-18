n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append([])

for j in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, start, target):
  visited = [False] * n #방문 배열
  stack = [start]

  while stack:
      node = stack.pop()
      if visited[node]== False:
          visited[node] = True
          if target in graph[node]:
              return True
          stack.extend(graph[node])
  return False

# A, B, C, D, E에 대한 친구 관계 확인
result = dfs(graph, 0, 1) and dfs(graph, 1, 2) and dfs(graph, 2, 3) and dfs(graph, 3, 4)

# 결과 출력
print(1 if result else 0)
