N, K = map(int, input().split())
baskets = []

# 입력 받기
for _ in range(N):
    candy, pos = map(int, input().split())
    baskets.append((pos, candy))

# 위치 기준으로 정렬
baskets.sort()

max_candies = 0
left = 0
right = 0
total_length = len(baskets)

# 왼쪽 바구니부터 시작
for left in range(total_length):
    # 현재 구간의 사탕 합계
    current_sum = 0
    # 오른쪽 바구니는 범위를 벗어나지 않을 때까지 이동
    right = left
    while right < total_length and baskets[right][0] - baskets[left][0] <= 2*K:
        current_sum += baskets[right][1]
        right += 1
    max_candies = max(max_candies, current_sum)

print(max_candies)