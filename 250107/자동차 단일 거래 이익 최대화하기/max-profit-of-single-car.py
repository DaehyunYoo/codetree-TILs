n = int(input())

nums = list(map(int, input().split()))

sale = 0
for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[j] - nums[i] > 0 and nums[j] - nums[i] > sale:
            sale = nums[j] - nums[i]

print(sale)
