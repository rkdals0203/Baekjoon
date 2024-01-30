array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array):
  if len(array)<=1:
    return array
  
  pivot = array[0]
  tail = array[1:]
  left_side = [i for i in tail if i<= pivot]
  right_side = [j for j in tail if j> pivot]
  
  return quick_sort(left_side)+[pivot]+quick_sort(right_side)

print(quick_sort(array))
  