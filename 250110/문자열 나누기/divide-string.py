n = input()
nums = list(map(int, input().split()))

result = ''
for i in nums:
    result += str(i)

for i in range(0, len(result), 5):
    print(result[i:i+5])