n, m = map(int, input().split())

def csc(x, y):
    result = 0
    for i in range(1, min(x, y)):
        if x % i == 0 and y % i == 0:
            result = i
    
    print(result)

csc(n, m)