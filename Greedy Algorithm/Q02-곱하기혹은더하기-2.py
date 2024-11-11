#1
s = input()
arr = []
for j in range(len(s)):
  arr.append(int(s[j]))
res = int(s[0])

for i in range (1, len(s)):
  print(res)
  print(arr[i])
  if res == 0 or res == 1:
    res = res + arr[i]
  elif arr[i] == 0 or arr[i] == 1:    
    res = res + arr[i]
  else:
    res = res * arr[i]
print(res)

#2 
s = input()
arr = []
for j in range(len(s)):
  arr.append(int(s[j]))
res = int(s[0])

for i in range (1, len(s)):
  add = res + arr[i]
  mod = res * arr[i]
  if add >= mod:
    res = add
  else:
    res = mod

print(res)