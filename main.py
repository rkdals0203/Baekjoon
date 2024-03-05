array = [5,7,9,0,3,1,6,2,4,8]

#퀵 정렬
def quick_sort(arr):
  if len(arr)<=1:
    return arr
  pivot = arr[0]
  new_arr = arr[1:]
  left_arr = []
  right_arr = []
  for i in new_arr:
    if i < pivot:
      left_arr.append(i)
    else:
      right_arr.append(i)
  return quick_sort(left_arr)+[pivot]+quick_sort(right_arr)

# #계수 정렬
# new_array = [0]*(max(array)+1)
# for i in array:
#   new_array[i]+=1
# for j in range(len(new_array)):
#   for k in range(new_array[j]):
#     print(j, end=" ")

# #선택 정렬
# for i in range(len(array)):
#   min_index = i
#   for j in range(i,len(array)):
#     if array[j] < array[min_index]:
#       min_index = j
#   array[i], array[min_index] = array[min_index], array[i]
# print(array)


#삽입 정렬
for i in range(1,len(array)): #1부터 끝까지 증가
  for j in range(i,0,-1): #i부터 1까지 감소
    if array[j] < array[j-1]: #오른쪽에 있는 원소가 왼쪽에 있는 원소보다 작다면?
      array[j],array[j-1] = array[j-1], array[j]
    else:
      break
print(array)
