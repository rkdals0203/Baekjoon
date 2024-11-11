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