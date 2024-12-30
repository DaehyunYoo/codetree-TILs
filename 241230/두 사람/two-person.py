# 입력 받기
age1, gender1 = input().split()
age2, gender2 = input().split()

# 정수로 변환
age1 = int(age1)
age2 = int(age2)

# 조건 체크
if (age1 >= 19 and gender1 == 'M') or (age2 >= 19 and gender2 == 'M'):
    print(1)
else:
    print(0)