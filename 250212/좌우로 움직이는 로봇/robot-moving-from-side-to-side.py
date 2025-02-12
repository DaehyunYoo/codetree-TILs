N, M = map(int, input().split())
position_a, position_b = [0], [0]

# 로봇 A 이동 기록
current_position = 0
for _ in range(N):
    t, d = input().split()
    t = int(t)
    for _ in range(t):
        if d == 'L':
            current_position -= 1
        else:
            current_position += 1
        position_a.append(current_position)

# 로봇 B 이동 기록
current_position = 0
for _ in range(M):
    t, d = input().split()
    t = int(t)
    for _ in range(t):
        if d == 'L':
            current_position -= 1
        else:
            current_position += 1
        position_b.append(current_position)

cnt = 0
time = min(len(position_a), len(position_b))
for i in range(time):
    if position_a[i] == position_b[i] and position_a[i - 1] != position_b[i - 1]:
        cnt += 1
    
print(cnt)