n = int(input())
students = []
for _ in range (n):
  name, score = input().split()
  students.append([name,int(score)])
array = sorted(students, key=lambda student: student[1]) #student:각 항목, student[1]:각 항목의 두 번째 원소

for student in array:
  print(student[0],end=" ")