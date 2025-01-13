n, m = map(int, input().split())

def square_(x, y):
    for _ in range(x):
        print('1' * y)

square_(n, m)