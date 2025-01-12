a = input()
b = input()
x, y = '', ''
for i in a:
    if i.isdigit():
        x += i

for i in b:
    if i.isdigit():
        y += i

print(int(x) + int(y))
