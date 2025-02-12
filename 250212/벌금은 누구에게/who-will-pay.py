N, M, K = map(int, input().split())

cnt = [0 for _ in range(N)]

nums = []

for _ in range(M):
    nums.append(int(input()))

result = -1
for i in nums:
    cnt[i-1] += 1
    if cnt[i-1] >= K:
        result = i
        break

print(result)

        
        