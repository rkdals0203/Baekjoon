# 완전 탐색
import sys
input = sys.stdin.readline

n = int(input())
count = 0
hour = n
minute = 59
second = 59

for i in range(hour+1):
  for j in range(minute+1):
    for k in range(second+1):
      if '3' in str(i) + str(j) + str(k):
        count+=1
print(count)