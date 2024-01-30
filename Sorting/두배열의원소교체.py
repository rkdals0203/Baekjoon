n,k = map(int,input().split())
arr_a=list(map(int,input().split()))
arr_b=list(map(int,input().split()))

arr_a.sort()
arr_b.sort(reverse=True)


for i in range (k):
  if arr_b[i]>arr_a[i]:
    arr_b[i],arr_a[i]=arr_a[i],arr_b[i]
  else: #a의 가장 작은 원소가 b이 가장 큰 원소보다 큰거니까 뒤에는 비교할 필요도 x
    break

print(sum(arr_a))