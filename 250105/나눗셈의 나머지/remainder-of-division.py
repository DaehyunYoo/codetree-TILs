a, b = map(int, input().split())
result = [0 for _ in range(b)]

while a > 1:
    result[a % b] += 1
    a //= b

sum = 0
for i in result:
    sum += (i**2)

print(sum)