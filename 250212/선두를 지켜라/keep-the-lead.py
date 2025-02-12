N, M = map(int, input().split())

# 각 시간별 위치 기록을 위한 리스트
position_a, position_b = [], []

# A의 이동 기록
current_pos = 0
for _ in range(N):
    v, t = map(int, input().split())  # 속도, 시간
    for _ in range(t):  
        current_pos += v
        position_a.append(current_pos)  

# B의 이동 기록
current_pos = 0
for _ in range(M):
    v, t = map(int, input().split())  # 속도, 시간
    for _ in range(t):  
        current_pos += v
        position_b.append(current_pos)

# 선두가 몇 번 바뀌었는지 계산
lead_changes = 0
prev_lead = None  # 이전 시간에서의 선두 상태 (None: 초기값)

for i in range(len(position_a)):  # 모든 시간에 대해 검사
    if position_a[i] > position_b[i]:
        current_lead = "A"
    elif position_a[i] < position_b[i]:
        current_lead = "B"
    else:
        current_lead = prev_lead  # 같다면 이전 선두 유지

    # 선두가 바뀌었는지 체크
    if prev_lead is not None and current_lead != prev_lead:
        lead_changes += 1

    prev_lead = current_lead  # 현재 상태를 다음 비교에 활용

print(lead_changes)
