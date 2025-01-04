lst = list(map(int, input().split()))
result = []

for i in lst:
    if i >= 250:
        break
    else:
        result.append(i)

sumation = sum(result)
mean = sum(result) / len(result)

print(sumation, mean)
    