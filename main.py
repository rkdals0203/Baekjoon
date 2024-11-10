n,k = map(int, input().split())
count = 0

if n<k:
  count = n-1

else:
  while n>=k:
    #빼는 부분(나눠지지 않을 때만 진짜로 뺌)
    target = (n//k)*k
    count += n-target
    n = target
    #나누는 부분
    n = n//k
    count+=1
print(count)