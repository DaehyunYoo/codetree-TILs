nums = list(map(int, input().split()))

num1, num2 = 0, 1000

for i in nums:
    if i > num1 and i < 500:
        num1 = i
    if i < num2 and i > 500:
        num2 = i

print(num1, num2)