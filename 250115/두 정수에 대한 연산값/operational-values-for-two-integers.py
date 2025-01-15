a, b = map(int, input().split())

def cal(x, y):
    print(min(x, y) * 2, max(x, y) + 25)

cal(a, b)