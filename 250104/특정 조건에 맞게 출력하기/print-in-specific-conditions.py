nums = list(map(int, input().split()))

for i in nums:
    if i == 0:
        break
    if i % 2 != 0:
        print((i+3), end=" ")
    else:
        print((i // 2), end=" ")