nums = list(input().split())

cnt = [0 for _ in range(10)]

for i in nums:
    if len(i) == 2:
        # print(int(i[0]))
        cnt[int(i[0]) - 1] += 1

for i in range(len(cnt)-1):
    print(f'{i+1} - {cnt[i]}')

