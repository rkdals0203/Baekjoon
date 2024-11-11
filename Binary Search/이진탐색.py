array = [0,2,5,8,10,16,20,21,22,30]

def binary_search(array, start, end, target):
  if start > end:
      return None
  mid = (start + end) // 2
  if array[mid] == target:
      return mid
  elif target > array[mid]:
      return binary_search(array, mid + 1, end, target)
  else:
      return binary_search(array, start, mid - 1, target)



print(binary_search(array,0,9,21))


#2
array = [0,2,4,6,8,10,12,14,16,18]

def binary_search2(start,end,target,array):
  if start > end: #종료조건
    return None

  middle = (start+end)//2 #start:0이고 end:9인 경우 middle은 버림해서 4
  if target==array[middle]:
    return middle
  elif target<array[middle]:
    return binary_search(start,middle-1,target,array)
  else:
    return binary_search(middle+1,end,target,array)


print(binary_search(0,9,6,array))