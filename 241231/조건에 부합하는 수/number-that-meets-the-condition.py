# 입력 받기
a = int(input())

# 결과를 저장할 리스트
result_numbers = []

# 1부터 a까지 순회하면서 조건 체크
for i in range(1, a + 1):
    # 모든 조건을 만족하지 않는지 확인하기 위한 플래그
    meets_any_condition = False
    
    # 조건 1: 짝수이면서 4의 배수가 아닌 수
    if i % 2 == 0 and i % 4 != 0:
        meets_any_condition = True
        continue
    
    # 조건 2: 8로 나눈 몫이 짝수인 수
    if (i // 8) % 2 == 0:
        meets_any_condition = True
        continue
    
    # 조건 3: 7로 나눈 나머지가 4보다 작은 수
    if (i % 7) < 4:
        meets_any_condition = True
        continue
    
    # 어떤 조건도 만족하지 않는 경우
    if not meets_any_condition:
        result_numbers.append(i)

# 결과 출력 (오름차순으로 정렬된 상태)
print(" ".join(map(str, result_numbers)))