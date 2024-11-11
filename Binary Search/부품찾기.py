n = int(input())
inv_arr = list(map(int,input().split()))
m = int(input())
ser_arr = list(map(int,input().split()))

def binary_search(array,start,end,target):
  if start>end:
    return "no"
  mid = (start+end)//2
  if array[mid] == target:
    return "yes"
  elif array[mid] > target:
    return binary_search(array,start,mid-1,target)
  else:
    return binary_search(array,mid+1,end,target)


for i in range(m):
  print(binary_search(inv_arr,0,len(ser_arr),ser_arr[i]), end=" ")

#2
n = int(input())
equips = list(map(int,input().split()))
m = int(input())
find_equips = list(map(int,input().split()))

def binary_search(arr,start,end,target):
  if start>end: #종료조건
    return None

  middle = (start+end)//2
  if target == arr[middle]:
    return middle
  elif target < arr[middle]: #목표 숫자가 중간보다 작으면
    return binary_search(arr,start,middle-1,target)
  else: #목표 숫자가 중간보다 크면
    return binary_search(arr,middle+1,end,target)

for i in find_equips:
  if binary_search(equips,0,n-1,i) == None:
    print("no",end=" ")
  else:
    print("yes",end=" ")