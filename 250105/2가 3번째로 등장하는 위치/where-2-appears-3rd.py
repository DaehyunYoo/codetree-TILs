n = int(input())

nums = list(map(int, input().split()))

cnt = 1
for i in range(len(nums)):
    if nums[i] == 2 and cnt != 3:
        cnt += 1
    elif nums[i] == 2 and cnt == 3:
        print(i+1)
        break
    else:
        continue


        