class Student():
    def __init__(self, name, height, weight):
        self.name = name
        self.height = int(height)
        self.weight = int(weight)
    
n = int(input())
students = []
for _ in range(n):
    name, height, weight = input().split()
    students.append(Student(name, int(height), int(weight)))

students.sort(key = lambda x: (x.height, -x.weight))

for i in students:
    print(i.name, i.height, i.weight)

