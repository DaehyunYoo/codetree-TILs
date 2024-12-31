# 입력받기
a, b = map(int, input().split())

# 정수 부분 계산
integer_part = a // b

# 소수점 이하 20자리 계산
decimal_part = ""
remainder = (a % b) * 10

for _ in range(20):  # 소수점 20자리까지 계산
    digit = remainder // b
    decimal_part += str(digit)
    remainder = (remainder % b) * 10

# 결과 출력
print(f"{integer_part}.{decimal_part}")