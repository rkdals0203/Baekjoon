#1
n,k = map(int, input().split())
count = 0

if k==1:
  count = n-1
else:
  while n!= 1:
    if n%k==0:
      n=n/k
    else:
      n=n-1
    count+=1
print(count)

#2
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