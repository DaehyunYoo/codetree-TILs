start, end = map(int, input().split())

cnt = 0
for i in range(start, end+1):
    result = 0
    # 자기 자신을 제외한 약수만 더하기 (1부터 i-1까지만 검사)
    for j in range(1, i):
        if i % j == 0:
            result += j
    # 약수의 합이 자기 자신과 같으면 완전수
    if result == i:
        cnt += 1
print(cnt)