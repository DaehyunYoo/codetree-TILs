scores = list(map(int, input().split()))

cnt = [0 for _ in range(11)]

for i in scores:
    if i == 0:
        break
    else:
        cnt[i // 10] += 1

# for i in range(1, len(cnt)):
#     print(cnt[i])
for i in range(len(cnt)-1, 0, -1):
    print(f'{i * 10} - {cnt[i]}')