N, H, T = map(int, input().split())
heights = list(map(int, input().split()))

min_cost = float('inf')
# 연속된 T개 이상의 구간을 찾기 위해 시작점을 이동
for i in range(N-T+1):
    cost = 0
    # 현재 시작점부터 T개의 밭에 대해 비용 계산
    for j in range(i, i+T):
        # 높이 차이의 절대값이 비용
        cost += abs(H - heights[j])
    min_cost = min(min_cost, cost)

if min_cost == float('inf'):
    print(-1)  # 불가능한 경우
else:
    print(min_cost)