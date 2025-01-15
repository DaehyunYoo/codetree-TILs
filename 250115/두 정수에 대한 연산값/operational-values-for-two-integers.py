a, b = map(int, input().split())

def cal(x, y):
    small = min(x, y) * 2
    larger = max(x, y) + 25
    return small, larger

result = cal(a, b)
print(*result)