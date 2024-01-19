n,m,current = map(int,input().split())
graph=[[] for _ in range(n+1)]

def dfs(current):
  visited[current]=1 #방문 표시
  ans_dfs.append(current) #방문 노드 추가
  for n in graph[current]:
    if visited[n]==0: #방문하지 않았던 노드라면
      dfs(n)

def bfs(current):
  q = []

  visited[current]=1
  q.append(current) #q에 초기데이터(들) 삽입
  ans_bfs.append(current)

  while q:
    current = q.pop(0)
    for n in graph[current]:
      if not visited[n]:
        q.append(n)
        ans_bfs.append(n)
        visited[n]=1



for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

# 1. 오름차순 정렬
for i in range(1,n+1):
  graph[i].sort()

visited=[0]*(n+1)
ans_dfs=[]
dfs(current)

visited=[0]*(n+1)
ans_bfs=[]
bfs(current)




print(*ans_dfs)
print(*ans_bfs)
