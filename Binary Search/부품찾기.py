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