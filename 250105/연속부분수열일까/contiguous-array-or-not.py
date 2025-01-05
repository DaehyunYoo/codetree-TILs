n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

is_subsequence = False
# A의 가능한 모든 시작 위치 확인
for i in range(n1 - n2 + 1):
    match = True
    # 현재 위치에서 B의 길이만큼 비교
    for j in range(n2):
        if A[i + j] != B[j]:
            match = False
            break
    if match:
        is_subsequence = True
        break

print("Yes" if is_subsequence else "No")
