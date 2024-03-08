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


#2
n,m = map(int,input().split())
arr = list(map(int,input().split()))
result=0

#가장 큰거 기준으로 이진탐색 진행
def binary_search(arr,start,end,target):
  global result
  if start>end:
    return None
  mid = (start+end)//2 #절단기 높이를 이진 탐색으로 찾기
  sum = 0
  for i in arr:
    if i-mid>0:
      sum+=i-mid
  if sum>=target: #떡이 더 많이 남거나 같으면
    result = mid #높이 업데이트
    return binary_search(arr,mid+1,end,target)
  else:
    return binary_search(arr,start,mid-1,target)

binary_search(arr,0,max(arr),m)
print(result)