# 입력 받기
n = int(input())

# 결과를 저장할 리스트
complete_numbers = []

# 1부터 n까지 순회하면서 온전수 찾기
for num in range(1, n + 1):
    # 온전수 조건 체크
    is_complete = True
    
    # 조건 1: 2로 나누어 떨어지는 경우
    if num % 2 == 0:
        is_complete = False
        continue
    
    # 조건 2: 일의 자리가 5인 경우
    if num % 10 == 5:
        is_complete = False
        continue
    
    # 조건 3: 3으로 나누어 떨어지면서 9로는 나누어 떨어지지 않는 수
    if num % 3 == 0 and num % 9 != 0:
        is_complete = False
        continue
    
    # 모든 조건을 통과한 경우 (온전수인 경우)
    if is_complete:
        complete_numbers.append(num)

# 결과 출력
print(" ".join(map(str, complete_numbers)))