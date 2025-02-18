N, K = map(int, input().split())
photos = [0] * 100

for _ in range(N):
    nums, alpha = input().split()
    if alpha == 'G':
        photos[int(nums) - 1] = 1
    else:
        photos[int(nums) - 1] = 2

answer = 0
for i in range(N-K+1):
    max_sum = 0
    for j in range(i, i+K+1):
        max_sum += photos[j]
    answer = max(answer, max_sum)

print(answer)