# deque는 자유자재로 스택처럼, 혹은 큐처럼 사용할 수 있는 자료구조.
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(y,x):
  queue = deque([(y,x)])
  while queue: #queue가 비어있지 않을 때 까지
    y,x = queue.popleft()
    for i in range(4):
      ny = y+dy[i]
      nx = x+dx[i]
      if ny>=0 and ny<n and nx>=0 and nx<m:
        if graph[ny][nx] == 1: #괴물 없는 부분이라면
          graph[ny][nx] = graph [y][x]+1
          queue.append((ny,nx))

# 미로 세팅
n,m = map(int,input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,input())))

bfs(0,0)
print(graph[n-1][m-1])