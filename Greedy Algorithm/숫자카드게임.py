n,m = map(int,input().split())
cards = []
for _ in range (n):
  lst = list(map(int,input().split()))
  min_value = min(lst)
  cards.append(min_value)
max_value = max(cards)
print(max_value)

#2
n,m = map(int,input().split())
arr = []
for _ in range(n):
  temp = min(list(map(int,input().split())))
  arr.append(temp)

print(max(arr))

#이중 반복문 이용
n,m = map(int,input().split())
arr = []
for _ in range(n):
  min = 10001
  data = list(map(int,input().split()))
  for i in range(m):
    if data[i]<min:
      min = data[i]
  arr.append(min)

print(max(arr))