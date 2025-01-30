class student():
    def __init__(self, name, height, weight):
        self.name = name
        self.height = int(height)
        self.weight = float(weight)

students = []
for i in range(5):
    name, height, weight = input().split()
    students.append(student(name, height, weight))

students.sort(key = lambda x: x.name)
print('name')
for i in students:
    print(i.name, i.height, i.weight)

print('')

students.sort(key = lambda x: -x.height)
print('height')
for i in students:
    print(i.name, i.height, i.weight)
