n = input()
arr = []
for i in n:
    arr.append(i)

# print(arr)
result = 0

for i in range(len(arr)):
    result = result * 2 + int(arr[i])

print(result)