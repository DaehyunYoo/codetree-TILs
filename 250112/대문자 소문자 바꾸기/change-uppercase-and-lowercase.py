A = input()

for i in A:
    if 'A' <= i and i <= 'Z':
        print(i.lower(), end='')
    else:
        print(i.upper(), end='')