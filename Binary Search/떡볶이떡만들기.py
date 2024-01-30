n, m = map(int,input().split()) #n:떡의 개수, m:필요한 길이
rice_cakes = list(map(int,input().split()))

def rice_cake_search(rice_cakes,start,end,target):
  if start>end:
    return None

  mid = (start+end)//2

  pieces = 0
  for i in range(n):
    if rice_cakes[i]-mid>0:
      pieces += rice_cakes[i]-mid

  if pieces == m:
    return mid
  elif pieces > m:
    return rice_cake_search(rice_cakes,mid+1,end,target)
  else:
    return rice_cake_search(rice_cakes,start,mid-1,target)

print(rice_cake_search(rice_cakes,0,max(rice_cakes),m))