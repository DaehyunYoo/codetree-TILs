N, S = map(int, input().split())
nums = list(map(int, input().split()))

total = sum(nums)
result = 10**9
for i in range(N):
    for j in range(N):
        if i != j:
            answer = total - (nums[i] + nums[j])
            result = min(result, abs(answer - S))

print(result)
            