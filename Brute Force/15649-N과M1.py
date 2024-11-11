def dfs(n,lst):
  #종료 조건 처리(정답에 관련)
  if n==M: #M개짜리 수열이 완성
    ans.append(lst)
    return
  #하부 함수 호출
  for j in range (1,N+1):
    if visited[j]==0:
      visited[j]=1
      dfs(n+1,lst+[j])
      visited[j]=0 #속도를 위한 처리라고함..

N,M = map(int,input().split())
ans=[]
visited=[0]*(N+1)

dfs(0,[])

for lst in ans:
  print(*lst)
