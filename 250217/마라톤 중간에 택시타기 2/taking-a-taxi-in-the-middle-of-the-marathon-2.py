N = int(input())

arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

result = 10**9
for i in range(1, N-1):  # 건너뛸 체크포인트 선택 (1번과 N번은 제외)
    distance = 0
    # 첫 번째부터 i-1번째 체크포인트까지
    for j in range(N-1):
        if j == i:  # 건너뛰는 체크포인트
            continue
        if j + 1 == i:  # 건너뛰는 체크포인트 다음으로 이동
            next_point = j + 2
        else:
            next_point = j + 1
        if next_point >= N:  # 범위 체크
            continue
        distance += abs(arr[j][0] - arr[next_point][0]) + abs(arr[j][1] - arr[next_point][1])
    
    result = min(distance, result)

print(result)