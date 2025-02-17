N = int(input())
nums = list(map(int, input().split()))

answer = 0
for i in range(N):
    for j in range(N):
        # 같은 숫자이거나 인접한 숫자인 경우 제외
        if i != j and abs(i - j) != 1:
            result = nums[i] + nums[j]
            answer = max(result, answer)

print(answer)