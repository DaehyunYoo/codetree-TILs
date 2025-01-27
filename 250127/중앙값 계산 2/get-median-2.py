n = int(input())
nums = [0]
nums_input = list(map(int, input().split()))
nums = nums + nums_input

for i in range(1, len(nums)):
    if i % 2 != 0:
        nums_res = nums[1:i+1]
        nums_res.sort()
        print(nums_res[i//2], end= ' ')