class Student:
    def __init__(self, height, weight, index):
        self.height = height
        self.weight = weight
        self.index = index


N = int(input())

nums = []
for i in range(N):
    height, weight = map(int, input().split())
    nums.append(Student(height, weight, i+1))

nums.sort(key = lambda x: (x.height, -x.weight))

for i in nums:
    print(i.height, i.weight, i.index)