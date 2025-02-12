N = int(input())
nums = []
ans, cnt = 0, 0

for i in range(N):
    nums.append(int(input()))
    if i == 0:
        cnt += 1
    elif (nums[i] < 0 and nums[i-1] < 0) or (nums[i] > 0 and nums[i-1] > 0):
        cnt += 1
    else:
        cnt = 1
    ans = max(ans, cnt)

print(ans)