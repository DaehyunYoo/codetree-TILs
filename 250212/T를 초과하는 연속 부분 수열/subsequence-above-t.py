N, T = map(int, input().split())
ans, cnt = 0, 0

nums = list(map(int, input().split()))

for i in range(N):
    if nums[i] > T:  
        if i > 0 and nums[i-1] + 1 == nums[i]:
            cnt += 1
        else:
            cnt = 1  # 새로 시작
    else:
        cnt = 0  
    
    ans = max(ans, cnt)

print(ans)