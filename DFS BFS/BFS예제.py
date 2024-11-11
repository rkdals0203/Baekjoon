# deque는 자유자재로 스택처럼, 혹은 큐처럼 사용할 수 있는 자료구조.
from collections import deque

def bfs(v):
  queue = deque([v])
  visited[v] = 1

  while queue: #큐가 비어있기 까지
    v = queue.popleft()
    print(v,end=" ")
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = 1


visited = [0]*9
graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

bfs(1)