num = input()
numbers = []
result = 0
for i in range(len(num)):
  numbers.append(int(num[i]))
numbers.sort()

for j in numbers:
  if result == 0:
    result += j
  else:
    a = result*j
    b = result+j
    result = max(a,b)
  
print(result)