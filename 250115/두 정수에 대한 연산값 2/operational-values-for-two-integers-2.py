a, b = map(int, input().split())

def abc(x, y):
    small = min(x, y) + 10
    large = max(x, y) * 2

    print(small, large)

abc(a, b)