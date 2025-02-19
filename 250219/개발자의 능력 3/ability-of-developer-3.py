nums = list(map(int, input().split()))

answer = 10**9
for i in range(len(nums)):
    for j in range(i, len(nums)):
        for k in range(j, len(nums)):
            if i != j and i != k and j != k and i != j != k:
                total = nums[i] + nums[j] + nums[k]
                answer = min(answer, abs((sum(nums) - total) - total))

print(answer)