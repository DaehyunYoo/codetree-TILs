x = input()

for i in x:
    if i.isdigit():
        print(i, end='')
    elif i.isalpha():
        print(i.lower(), end='')