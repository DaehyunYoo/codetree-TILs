N, T = map(int, input().split())
ans, cnt = 0, 0

nums = list(map(int, input().split()))

for i in range(len(nums)):
    if i == 0:
        cnt += 1
    elif nums[i-1] + 1 == nums[i]:
        cnt += 1
    else:
        cnt = 1
    ans = max(ans, cnt)

print(ans)