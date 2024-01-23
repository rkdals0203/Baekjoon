N = int(input())
f = list(map(int,input().split()))
f.sort() # 오름차순 정렬
count = 0 # 현재 그룹에 있는 사람들
ans = 0 # 그룹 개수

for i in f:
  count+=1
  if count >= i: # 현재 그룹에 있는 사람들 수가 가장 큰 공포도보다 크거나 같으면
    ans += 1 # 출발!
    count = 0
  

