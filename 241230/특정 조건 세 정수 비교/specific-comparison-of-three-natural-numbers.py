a, b, c = map(int, input().split())

result = []
if a == min(a, b, c):
    result.append(1)
else:
    result.append(0)

if a == b == c:
    result.append(1)
else:
    result.append(0)

print(*result)