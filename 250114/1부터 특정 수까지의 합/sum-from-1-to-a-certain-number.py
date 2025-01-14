N = int(input())

def fun(x):
    sumation = 0
    for i in range(1, x+1):
        sumation += i
    return sumation // 10

print(fun(N))