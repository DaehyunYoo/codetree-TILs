nums = input().split()
cnt = [0] * 10  # 0부터 9까지의 카운트를 저장할 리스트

for num in nums:
    # 문자열을 정수로 변환
    n = int(num)
    # 십의 자리가 있다면 (10 이상이면)
    if n >= 10:
        cnt[n // 10] += 1  # 십의 자리 수를 카운트
    # elif n > 0:  # 0보다 큰 한 자리 수라면
    #     cnt[n] += 1  # 해당 숫자를 카운트

# 결과 출력
for i in range(1, 10):
    print(f'{i} - {cnt[i]}')