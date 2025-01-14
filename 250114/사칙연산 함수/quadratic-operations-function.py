a, o, c = input().split()

def plus(x, y):
    return int(x) + int(y)

def minus(x, y):
    return int(x) - int(y)

def divide(x, y):
    if int(y) == 0:  # 0으로 나누는 경우 처리
        return "나눗셈 불가"
    return int(x) // int(y)

def multiple(x, y):
    return int(x) * int(y)

if o not in ['+', '-', '/', '*']:
    print('False')
else:
    try:
        if o == '+':
            print(f'{a} {o} {c} = {plus(a, c)}')
        elif o == '-':
            print(f'{a} {o} {c} = {minus(a, c)}')
        elif o == '/':
            print(f'{a} {o} {c} = {divide(a, c)}')
        else:
            print(f'{a} {o} {c} = {multiple(a, c)}')
    except ValueError:  # 숫자가 아닌 입력을 처리
        print('숫자를 입력해주세요')