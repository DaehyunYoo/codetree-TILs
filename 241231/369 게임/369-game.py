# 입력 받기
n = int(input())

# 1부터 n까지 반복
for i in range(1, n + 1):
   # 현재 숫자가 3의 배수인지 확인
   if i % 3 == 0:
       print(0, end=' ')
       continue
       
   # 현재 숫자에 3,6,9가 포함되어 있는지 확인
   num_str = str(i)
   if '3' in num_str or '6' in num_str or '9' in num_str:
       print(0, end=' ')
   else:
       print(i, end=' ')