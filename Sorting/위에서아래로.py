n = int(input())
array = []
for _ in range (n):
  num = int(input())
  array.append(num)
array.sort(reverse=True)
print(*array)


#2
n = int(input())
arr = []
for _ in range(n):
  arr.append(int(input()))

#기본 정렬 라이브러리로 구현
def basic_sort(arr):
  arr.sort(reverse=True)
  print(*arr)

#선택 정렬로 구현
def selection_sort(arr):
  for i in range(n):
    for j in range(i+1,n):
      max_index = i
      if arr[j] > arr[max_index]: #j번째 요소가 기존 max_index보다 더 크면
        max_index = j #max_index가 j가 됨
      arr[i], arr[max_index] = arr[max_index], arr[i]
  return(arr)

#삽입 정렬로 구현
def insertion_sort(arr):
  for i in range(n):
    for j in range(i,0,-1):
      if arr[j] > arr[j-1]: #j번째가 j-1보다 크면 
        arr[j],arr[j-1] = arr[j-1],arr[j] #서로 교체
      else: #아니면 멈추기
        break
  return(arr)

#퀵 정렬로 구현
def quick_sort(arr):
  if len(arr)<=1:
    return arr
  pivot = arr[0]
  remainder_arr = arr[1:]
  left_arr = []
  right_arr = []
  for i in remainder_arr:
    if i>pivot:
      left_arr.append(i)
    else:
      right_arr.append(i)
  return quick_sort(left_arr)+[pivot]+quick_sort(right_arr)

#계수 정렬로 구현
def count_sort(arr):
  count = [0]*(max(arr)+1)
  sorted_arr = []
  for i in arr:
    count[i]+=1
  for j in range(len(count)-1,-1,-1): #count길이-1 부터 0까지 1씩 감소
    for _ in range(count[j]):
      sorted_arr.append(j)
  return(sorted_arr)



