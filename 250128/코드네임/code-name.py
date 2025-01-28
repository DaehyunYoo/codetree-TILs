class result:
    def __init__(self, codename='', score= 0):
        self.codename = codename
        self.score = score


students = []
for _ in range(5):
    name, score = input().split()
    students.append(result(name, int(score)))

min_idx = 0
for i in range(5):
    if students[min_idx].score > students[i].score:
        min_idx = i

print(students[min_idx].codename, students[min_idx].score)


