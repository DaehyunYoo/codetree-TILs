n = int(input())

nums = list(map(int, input().split()))

cnt = [0 for _ in range(10)]

for i in nums:
    cnt[i] += 1

for i in range(1, len(cnt)):
    print(cnt[i])