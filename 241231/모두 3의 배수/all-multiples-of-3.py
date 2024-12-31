# 5개의 정수를 입력받아 리스트로 저장
numbers = [int(input()) for _ in range(5)]

# 모든 수가 3의 배수인지 확인
all_multiples_of_three = all(num % 3 == 0 for num in numbers)

# 결과 출력
if all_multiples_of_three:
    print(1)
else:
    print(0)