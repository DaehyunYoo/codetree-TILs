a, b, c = input().split()

class result:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time

result1 = result(a, b, c)
print(f'secret code : {result1.code}')
print(f'meeting point : {result1.place}')
print(f'time : {result1.time}')