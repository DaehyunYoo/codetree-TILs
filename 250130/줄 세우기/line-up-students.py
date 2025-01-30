class Student:
    def __init__(self, height, weight, index):
        self.height = int(height)    # 문자열을 정수로 변환
        self.weight = int(weight)    # 문자열을 정수로 변환
        self.index = index

N = int(input())
students = []

for i in range(N):
    height, weight = input().split()
    students.append(Student(height, weight, i+1))

# 정렬 기준을 내림차순(-x.height)으로 변경하고, 몸무게도 내림차순으로 변경
students.sort(key=lambda x: (-x.height, -x.weight, x.index))

for student in students:
    print(student.height, student.weight, student.index)  # 문제 출력 형식에 맞게 번호만 출력