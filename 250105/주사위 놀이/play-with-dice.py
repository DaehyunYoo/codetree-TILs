nums = list(map(int, input().split()))

cnt = [0 for _ in range(6)]

for i in nums:
    cnt[i-1] += 1

for i in range(6):
    print(f'{i+1} - {cnt[i]}')