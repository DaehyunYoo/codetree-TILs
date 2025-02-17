N = int(input())
nums = list(map(int, input().split()))

min_length = float('inf')

for i in range(N):
    answer = 0
    house = i + 1  # 집 위치는 1부터 시작
    for j in range(N):
        answer += abs(house - (j + 1)) * nums[j]
    min_length = min(min_length, answer)

print(min_length)