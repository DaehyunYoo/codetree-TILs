a, b = map(int, input().split())

c = a+b
sum = 0
for i in str(c):
    if i == '1':
        sum += 1

print(sum)