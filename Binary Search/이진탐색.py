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