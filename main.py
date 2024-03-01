def dfs(y,x):
  #정해진 틀 이외의 접근은 바로 리턴해버림
  if y<0 or y>=n or x<0 or x>=m:
    return False
  #현재 좌표가 0이라면
  if graph[y][x] == 0:
    graph[y][x] = 1
    dfs(y-1,x)
    dfs(y+1,x)
    dfs(y,x-1)
    dfs(y,x+1)
    return True
  #현재 좌표가 1이라면
  else:
    return False

#그래프 만들기
n,m = map(int,input().split())
graph= []
for _ in range (n):
  graph.append(list(map(int,input())))

count = 0 
for i in range(n):
  for j in range(m):
    if dfs(i,j)==True:
      count+=1

print(count)





#visited 필요 없음. 왜냐하면 그래프에서 1로 표시해버리면 그만이거든
#또한, 그래프는 인접리스트가 아니라 좌표임.
visited = [0]*9