a, b = map(int, input().split())

lst = []
for i in range(a, b+1):
    if i % 2 == 0:
        lst.append(i)

lst.sort(reverse=True)

for i in range(1, 10):
    for j in lst:
        if j != min(lst):
            print(f'{j} * {i} = {i * j} /', end=" ")
        else:
            print(f'{j} * {i} = {i * j}', end=" ")
    print()