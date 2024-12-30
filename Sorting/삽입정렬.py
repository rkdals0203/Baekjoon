array = [7,5,9,0,3,1,6,2,4,8]

def insertion_sort(array):
  for i in range (1, len(array)):
    for j in range (i, 0, -1): #i부터 1까지 감소
      if array[j] < array[j-1]:
        array[j],array[j-1] = array[j-1],array[j]
  return array

print(insertion_sort(array))

#2
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
  for j in range(i,0,-1):
    if array[j]<array[j-1]:
      array[j],array[j-1] = array[j-1],array[j]
    else:
      break

print(array)

#3
array = [10,5,4,3,1,9,7,8,6,2]

for i in range (1, len(array)):
    for j in range (i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] =array[j-1], array[j]
        else:
            break

print(array)