N,M,K = map(int,input().split()) #5 8 3
arr = list(map(int,input().split())) #2 4 5 4 6
arr.sort(reverse=True) # 6 5 4 4 2
# 답: 6+6+6+5+6+6+6+5
first = arr[0]
second = arr[1]
inner_count = 0
outer_count = 0
ans = 0

while outer_count < M:
  while inner_count < K:
    ans += first
    inner_count += 1
    outer_count += 1
  ans+=second
  outer_count += 1
  inner_count = 0
  if outer_count == M:
    break

print(ans)