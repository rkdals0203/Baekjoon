n = int(input())
students = []
for _ in range (n):
  name, score = input().split()
  students.append([name,int(score)])
array = sorted(students, key=lambda student: student[1]) #student:각 항목, student[1]:각 항목의 두 번째 원소

for student in array:
  print(student[0],end=" ")


#2
n = int(input())
arr = []
for _ in range(n):
  temp = list(input().split())
  arr.append(temp)

#기본 정렬 라이브러리로 구현
def basic_sort(arr):
  arr.sort(key = lambda student: int(student[1])) #람다 함수 이용
  for student in arr:
    print(student[0],end=" ")

#선택 정렬로 구현
def selection_sort(arr):
  for i in range(n):
    for j in range(i+1,n):
      max_index = i
      if arr[j][1] < arr[max_index][1]: #j번째 요소의 점수가 기존 max_index보다 더 크면
        max_index = j #max_index가 j가 됨
      arr[i], arr[max_index] = arr[max_index], arr[i]
  for k in range(n):
    print(arr[k][0],end=" ")

#삽입 정렬로 구현
def insertion_sort(arr):
  for i in range(n):
    for j in range(i,0,-1):
      if arr[j][1] < arr[j-1][1]: #j번째의 점수가 j-1보다 작으면 
        arr[j],arr[j-1] = arr[j-1],arr[j] #서로 교체
      else: #아니면 멈추기
        break
  for k in range(n):
    print(arr[k][0],end=" ")

#퀵 정렬로 구현
def quick_sort(arr):
  if len(arr)<=1:
    return arr
  pivot = arr[0]
  remainder_arr = arr[1:]
  left_arr = []
  right_arr = []
  for i in remainder_arr:
    if i[1]<pivot[1]:
      left_arr.append(i)
    else:
      right_arr.append(i)
  return quick_sort(left_arr)+[pivot]+quick_sort(right_arr)

# sorted_arr = quick_sort(arr)
# for i in sorted_arr:
#   print(i[0],end=" ")

#계수 정렬로 구현
def count_sort(arr):
  count = [[] for _ in range(int(max(arr, key= lambda student: student[1])[1])+1)]
  for i in range(n):
    count[int(arr[i][1])].append(arr[i][0])
  for j in count:
    if j:
      for k in range(len(j)):
        print(j[k],end=" ")

count_sort(arr)


