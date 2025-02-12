N, M = map(int, input().split())

MAX_T = 1000000
pos_a, pos_b = [0] * (MAX_T+1), [0] * (MAX_T + 1) 
time_a, time_b = 1, 1

for _ in range(N):
    d, t = input().split()
    if d == 'R':
        for _ in range(int(t)):
            pos_a[time_a] = pos_a[time_a - 1] + 1
            time_a += 1
    else:
        for _ in range(int(t)):
            pos_a[time_a] = pos_a[time_a - 1] - 1
            time_a += 1

for _ in range(M):
    d, t = input().split()
    if d == 'R':
        for _ in range(int(t)):
            pos_b[time_b] = pos_b[time_b - 1] + 1
            time_b += 1
    else:
        for _ in range(int(t)):
            pos_b[time_b] = pos_b[time_b - 1] - 1
            time_b += 1
    

ans = -1
for i in range(1, time_a):
    if pos_a[i] == pos_b[i]:
        ans = i
        break

print(ans)