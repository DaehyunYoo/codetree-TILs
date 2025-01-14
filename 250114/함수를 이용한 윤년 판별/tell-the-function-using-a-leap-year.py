y = int(input())

def func(x):
    if x % 100 == 0 and x % 400 != 0:
        return False

    if x % 4 == 0:
        return True
    
    return False

if func(y):
    print('true')
else:
    print('false')