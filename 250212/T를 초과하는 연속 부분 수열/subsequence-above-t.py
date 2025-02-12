N, T = map(int, input().split())
nums = list(map(int, input().split()))

ans, cnt = 0, 0

for i in range(N):
    if nums[i] > T:  # T보다 큰 숫자인지 확인
        if i > 0 and nums[i-1] > T:  # 바로 이전 숫자도 T보다 크다면 연속된 구간
            cnt += 1
        else:
            cnt = 1  # 새 연속 부분 수열 시작
    else:
        cnt = 0  # 연속 부분 수열이 끊김
    
    ans = max(ans, cnt)

print(ans)
