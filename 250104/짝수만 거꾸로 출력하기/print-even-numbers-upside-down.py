n = int(input())
nums = list(map(int, input().split()))
result = []
for i in nums:
    if i % 2 == 0:
        result.append(i)

print(*result[::-1])