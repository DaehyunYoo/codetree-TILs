a, b = map(int, input().split())

def abc(x, y):
    small = min(x, y) + 10
    large = max(x, y) * 2

    if x > y:
        x = large
        y = small
    else:
        x = small
        y = large

    print(x, y)

abc(a, b)