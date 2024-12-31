# 3의 배수와 5의 배수의 개수를 저장할 변수 초기화
count_3 = 0
count_5 = 0

# 10개의 수 입력받기
for _ in range(10):
   num = int(input())
   
   # 3의 배수 확인
   if num % 3 == 0:
       count_3 += 1
       
   # 5의 배수 확인
   if num % 5 == 0:
       count_5 += 1

# 결과 출력
print(count_3, count_5)