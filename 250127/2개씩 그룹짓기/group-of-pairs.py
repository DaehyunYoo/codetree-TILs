N = int(input())

nums = list(map(int, input().split()))

nums.sort()
group_max = 0

for i in range(N):
    group_sum = nums[i] + nums[2*N - 1 -i]
    if group_sum > group_max:
        group_max = group_sum
    
print(group_max)