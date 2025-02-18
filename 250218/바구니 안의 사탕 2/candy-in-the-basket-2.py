# 입력 받기
N, K = map(int, input().split())
# 좌표가 음수일 수 있으므로, 딕셔너리 사용
candies = {}

# 사탕 정보 입력받기
min_pos = float('inf')
max_pos = float('-inf')
for _ in range(N):
    cnt, pos = map(int, input().split())
    candies[pos] = cnt
    min_pos = min(min_pos, pos)
    max_pos = max(max_pos, pos)

max_sweets = 0
# 가능한 모든 중심점에 대해 검사
for c in range(min_pos, max_pos + 1):
    # 현재 중심점에서 구간 [c-K, c+K] 내의 사탕 개수 계산
    current_sweets = 0
    for pos in candies:
        if c - K <= pos <= c + K:
            current_sweets += candies[pos]
    max_sweets = max(max_sweets, current_sweets)

print(max_sweets)