n,k = map(int,input().split())
count = 0

while n > 1:
  if n%k == 0:
    n = n/k
    count+=1
  else:
    n-=1
    count+=1

print(count)

#2
import sys
input = sys.stdin.readline

count = 0
n,k = map(int,input().split())

while n!=1:
  if n%k==0:
    n = n//k
    count+=1
  else:
    n = n-1
    count+=1

print(count)