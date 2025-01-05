nums = list(input().split())

cnt = [0 for _ in range(10)]

for i in nums:
    if len(i) == 2:
        # print(int(i[0]))
        cnt[int(i[0]) - 1] += 1

for i in range(1, 10):
    print(f'{i} - {cnt[i-1]}')

