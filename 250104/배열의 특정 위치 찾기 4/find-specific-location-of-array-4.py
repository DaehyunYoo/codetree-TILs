nums = list(map(int, input().split()))
cnt = 0
lst = []
for i in nums:
    if i == 0:
        break
    else:
        if i % 2 == 0:
            cnt += 1
            lst.append(i)

print(cnt, sum(lst))