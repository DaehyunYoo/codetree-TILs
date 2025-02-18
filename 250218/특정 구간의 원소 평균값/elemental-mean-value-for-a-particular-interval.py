N = int(input())
nums = list(map(int, input().split()))

cnt = 0

for i in range(N):
    term = []
    for j in range(i, N):
        term.append(nums[j])
        mean = sum(term) / len(term)
        if mean in term:
            cnt += 1

print(cnt)