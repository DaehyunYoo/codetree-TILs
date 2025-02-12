N = int(input())
nums = []
results = []
cnt = 1

for i in range(N):
    nums.append(input())
    if i == 0:
        results.append(cnt)
    elif nums[i] == nums[i-1]:
        cnt += 1
        results.append(cnt)
    else:
        cnt = 1
        results.append(cnt)
        
print(max(results))