arr = list(map(int, input().split()))

result = []
for elem in arr:
    if elem == 0:
        break
    result.append(elem)

print(*result[::-1])