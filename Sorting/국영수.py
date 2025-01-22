n = int(input())
students = []

def sort_students(student):
    return -student[1], student[2], -student[3], student[0]

for _ in range(n):
    students.append(input().split())

students.sort(key=lambda student: (-student[1], student[2], -student[3], student[0]))

print(students)