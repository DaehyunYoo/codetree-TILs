nums = list(map(int, input().split()))

total, average = 0, 0
for i in range(1, len(nums), 2):
    total += nums[i]

total_3, cnt = 0, 0
for i in range(2, len(nums), 3):
    total_3 += nums[i]
    cnt += 1

print(f'{total} {(total_3 / cnt):.1f}')