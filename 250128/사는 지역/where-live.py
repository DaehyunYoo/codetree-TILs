n = int(input())

class result:
    def __init__(self, name, num, region):
        self.name = name
        self.num = num
        self.region = region

data = []
for _ in range(n):
    name, num, region = input().split()
    data.append(result(name, num, region))

max_idx = 0
for i in range(n):
    if data[i].name > data[max_idx].name:
        max_idx = i

print(f'name {data[max_idx].name}')
print(f'addr {data[max_idx].num}')
print(f'city {data[max_idx].region}')