# A 판정 카운트 변수 초기화
count_a = 0

# 3명의 상태 확인
for _ in range(3):
    # 증상과 체온 입력 받기
    symptom, temp = input().split()
    temp = float(temp)
    
    # 진료소 분류
    if symptom == 'Y' and temp >= 37:
        # A 진료소 케이스
        count_a += 1

# 위급상황 판단 및 출력
if count_a >= 2:
    print('E')  # Emergency
else:
    print('N')  # Normal