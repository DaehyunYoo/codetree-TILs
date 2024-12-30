# 연도 입력 받기
year = int(input())

# 윤년 판단 로직
is_leap_year = False

if year % 4 == 0:  # 4로 나누어 떨어지면 일단 윤년
    is_leap_year = True
    if year % 100 == 0:  # 100으로 나누어 떨어지면
        if year % 400 != 0:  # 400으로 나누어 떨어지지 않으면 평년
            is_leap_year = False

# 결과 출력
print(str(is_leap_year).lower())