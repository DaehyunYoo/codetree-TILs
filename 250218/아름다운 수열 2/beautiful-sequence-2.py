N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
for i in range(0, N - M + 1):
    if sorted(A[i:i+M]) == sorted(B):
        cnt += 1

print(cnt)
    

