a, o, c = input().split()

def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def divide(x, y):
    return x // y

def multiple(x, y):
    return int(x)*int(y)


if o not in ['+', '-', '/', '*']:
    print('False')
else:
    if o == '+':
        print(f'{a} {o} {c} = {plus(a, c)}')
    elif o == '-':
        print(f'{a} {o} {c} = {minus(a, c)}')
    elif o == '/':
        print(f'{a} {o} {c} = {divide(a, c)}')
    else:
        print(f'{a} {o} {c} = {multiple(a, c)}')
