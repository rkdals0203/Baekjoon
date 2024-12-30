array = [7,5,9,0,3,1,6,2,4,8]

def selection_sort(array):
  for i in range (len(array)):
    min_index = i
    for j in range (i+1, len(array)):
      if array[min_index]>array[j]:
        min_index = j
    array[min_index],array[i]=array[i],array[min_index]
  return array

print(selection_sort(array))

#2
array = [10,5,4,3,1,9,7,8,6,2]

for i in range (len(array)):
    min_index = i
    for j in range (i+1, len(array)):
        if array[j] < array[min_index]:
            min_index = j
    if array[i] > array[min_index] :
        array[i], array[min_index] = array[min_index], array[i]

print(array)