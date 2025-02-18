N, K = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0
for i in range(N-K+1):
    sum_result = 0
    
    for j in range(i, i + K):
        sum_result += nums[j]
        
    answer = max(sum_result, answer)

print(answer)