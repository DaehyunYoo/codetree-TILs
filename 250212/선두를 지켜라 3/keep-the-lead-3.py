N, M = map(int, input().split())
A, B = [], []

current_pos = 0
for _ in range(N):
    v, t = map(int, input().split())
    for i in range(1, t+1):
        current_pos += v
        A.append(current_pos)

current_pos = 0
for _ in range(M):
    v, t = map(int, input().split())
    for i in range(1, t+1):
        current_pos += v
        B.append(current_pos)

max_time = max(len(A), len(B))

if max_time > len(A):
    A = A + [A[-1]] * (max_time - len(A))
else:
    B = B + [B[-1]] * (max_time - len(B))


top = [2]
for i in range(max_time):
    if A[i] > B[i]:
        top.append(0)
    elif B[i] > A[i]:
        top.append(1)
    else:
        top.append(2)

cnt = 0
for i in range(1, len(top)):
    if top[i-1] != top[i]:
        cnt += 1
print(cnt)