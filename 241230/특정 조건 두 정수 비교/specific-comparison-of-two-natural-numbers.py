a, b = map(int, input().split())
result = []
if a < b:
    result.append(1)
else:
    result.append(0)

if a == b:
    result.append(1)
else:
    result.append(0)

print(*result)