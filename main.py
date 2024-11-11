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