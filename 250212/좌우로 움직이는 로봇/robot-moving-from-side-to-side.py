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

# print(position_a)
# print(position_b)

cnt = 0
time = max(len(position_a), len(position_b))
# 이동이 멈추면 마지막 위치 고정

# 마지막 위치로 리스트 확장
position_a += [position_a[-1]] * (time - len(position_a))
position_b += [position_b[-1]] * (time - len(position_b))

for i in range(1, time):
    if position_a[i] == position_b[i] and position_a[i - 1] != position_b[i - 1]:
        cnt += 1

print(cnt)