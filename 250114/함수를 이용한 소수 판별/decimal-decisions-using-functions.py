a, b = map(int, input().split())

def func(x):
    if x < 2:
        return False
        
    for i in range(2, x):
        if x % i == 0:
            return False

    return True

result = 0
for i in range(a, b+1):
    if func(i):
        result += i

print(result)