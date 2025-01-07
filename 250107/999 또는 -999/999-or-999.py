nums = list(map(int, input().split()))

min_num, max_num = nums[0], nums[0]
for i in nums:
    if i == 999 or i == -999:
        print(max_num, min_num)
        break
        
    else:
        if min_num > i:
            min_num = i
        if max_num < i:
            max_num = i
