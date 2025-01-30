class c:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    

n = int(input())
students = []
for _ in range(n):
    name, height, weight = input().split()
    students.append(c(name, height, weight))

students.sort(key = lambda x: x.height)

for i in students:
    print(i.name, i.height, i.weight)