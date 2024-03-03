n, m = map(int, input().split())
graph = []

for i in range(n + 1):
    if i == 0:
        row = [0] * (m + 1)
    else:
        row = [0]
        row.extend(list(map(int, input())))
    graph.append(row)

dy = [-1, 1, 0, 0]  # 상하
dx = [0, 0, -1, 1]  # 좌우

def isInrange(y, x):
    return x >= 1 and y >= 1 and x <= m and y <= n

def dfs(y, x):
    if not isInrange(y, x) or graph[y][x] == 0:
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if isInrange(ny, nx) and graph[ny][nx] == 1:
            graph[ny][nx] = graph[y][x] + 1
            dfs(ny, nx)

dfs(1, 1)
print(graph[n][m])


#2
# deque는 자유자재로 스택처럼, 혹은 큐처럼 사용할 수 있는 자료구조.
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(y,x):
  queue = deque([(y,x)]) #처음으로 (y,x) 튜플을 큐에 삽입하고 시작  
  while queue: #큐가 비어있기 까지
    (y,x) = queue.popleft()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if nx>=0 and nx<m and ny>=0 and ny<n: #공간을 벗어나지 않은 경우
        if graph[ny][nx] == 1: #괴물이 없는 부분이라면
          graph[ny][nx] = graph[y][x] + 1
          queue.append((ny,nx))

  print(graph[n-1][m-1]) # 미로 끝의 숫자 출력


# 미로 세팅
n,m = map(int,input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,input())))

bfs(0,0)
