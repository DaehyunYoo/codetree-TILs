N = int(input())
nums = list(map(int, input().split()))

answer = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if nums[i] <= nums[j] <= nums[k]:
                answer += 1

print(answer)