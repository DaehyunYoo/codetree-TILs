x, y = input().split()
a, b = '', ''
for i in x:
    if i.isdigit():
        a += i
    else:
        break

for i in y:
    if i.isdigit():
        b += i
    else:
        break

print(int(a) + int(b))

