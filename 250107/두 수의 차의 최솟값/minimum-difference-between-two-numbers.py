n = int(input())

nums = list(map(int, input().split()))

result = 100
for i in range(len(nums)):
    for j in range(i, len(nums)):
        if i != j and abs(nums[i] - nums[j]) < result:
            result = abs(nums[i] - nums[j])

print(result)