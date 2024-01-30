array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array):
  if len(array)<=1:
    return array
  pivot = array[0]
  tail = array[1:]
  left_side = [i for i in tail if i<=pivot]
  right_side = [j for j in tail if j>pivot]
  return quick_sort(left_side)+[pivot]+quick_sort(right_side)

def insertion_sort(array):
  for i in range(1, len(array)): #0번째는 이미 정렬 되어 있다고 가정
    for j in range(i,0,-1): #i부터 왼쪽으로 순회
      if array[j] <= array[j-1]: #순회하는 j가 바로 왼쪽보다 작으면 바꾸기
        array[j],array[j-1] = array[j-1],array[j]
      else: #j가 바로 왼쪽보다 더 크다? 나머지는 비교할 필요도 없음
        break
  return array

def selection_sort(array):
  for i in range(len(array)):
    min_index = i
    for j in range(i,len(array)):
      if array[min_index]>array[j]:
        min_index = j
        array[i]=array[min_index]
  return array


print(quick_sort(array))
print(insertion_sort(array))
print(selection_sort(array))
