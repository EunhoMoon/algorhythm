"""
https://www.acmicpc.net/problem/5597
"""

students = [i for i in range(1, 31)]

while len(students) > 2:
    student = int(input())
    students.remove(student)

for student in students:
    print(student)
