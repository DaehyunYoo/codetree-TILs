code, color, time = input().split()

class result:
    def __init__(self, code, color, time):
        self.code = code
        self.color = color
        self.time = time


result1 = result(code, color, time)

print(f'code : {result1.code}')
print(f'color : {result1.color}')
print(f'second : {result1.time}')