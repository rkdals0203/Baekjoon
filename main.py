s = input()
lst = []

for i in s:
  i=int(i)
  lst.append(i)

for j in range (len(lst)-1):
  if (lst[j]+lst[j+1]>=lst[j]*lst[j+1]):
    lst[j+1] = lst[j]+lst[j+1]
  else:
    lst[j+1] = lst[j]*lst[j+1]

print(lst[-1])
#커밋
  
  
