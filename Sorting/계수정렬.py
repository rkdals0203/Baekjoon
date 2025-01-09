array = [7,5,9,0,3,1,6,2,4,8]

def count_sort(array):
  count_arr = [0]*(max(array)+1)
  for i in array:
    count_arr[i]+=1
  for j in range(len(count_arr)):
    for _ in range(count_arr[j]):
      print(j,end=" ")

count_sort(array)


#2
array = [5,7,9,0,3,1,6,2,4,8]
index_arr = [0]*(max(array)+1)

for i in array:
  index_arr[i] += 1

for j in range(len(index_arr)):
  for k in range(index_arr[j]):
    print(j, end=" ")
    
#3
array = [1,231,13,2,3,4,5,6,7,8,9,10] #len(array) == 12
indexes = [0]*(max(array)+1) #232개의 0배열
sorted_arr = []

for i in range(len(array)): #0부터 11까지
    index = array[i]
    indexes[index] += 1
    
for j in range(len(indexes)): #11
    if indexes[j] != 0:
        sorted_arr.append(j)

print(sorted_arr)

#4
array = [5,7,9,0,3,1,6,2,4,8]
index_arr = [0]*(max(array)+1)
sorted_arr = []

for i in array:
  index_arr[i] += 1

for j in range(len(index_arr)):
  for k in range(index_arr[j]):
    sorted_arr.append(j)
    