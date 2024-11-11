def dfs(v):
  if visited[v] == 1: #이미 방문 했다면
    return False
  else: #처음 방문하는거라면
    visited[v] = 1
    print(v,end=" ")
    for i in graph[v]:
      dfs(i)


visited = [0]*7
graph = [
  [],
  [2,3],
  [1,6],
  [1,5],
  [],
  [3],
  [2]
]

dfs(1)