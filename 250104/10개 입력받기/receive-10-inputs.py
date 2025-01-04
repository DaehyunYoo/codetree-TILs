nums = list(map(int, input().split()))
result = []
for i in nums:
    if i == 0:
        break
        total = sum(result)
        average = total / len(result)
        print(f'{total} {average:.1f}')
    else:
        result.append(i)

total = sum(result)
average = total / len(result)
print(f'{total} {average:.1f}')