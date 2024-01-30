n = int(input())
array = []
for _ in range (n):
  num = int(input())
  array.append(num)
array.sort(reverse=True)
print(*array)