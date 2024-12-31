n = int(input())
cnt = 0

for i in range(1, n+1):
    # 윤년 조건:
    # 1. 4의 배수이면서
    #    - 100의 배수가 아니거나
    #    - 400의 배수인 경우
    if (i % 4 == 0) and (i % 100 != 0 or i % 400 == 0):
        cnt += 1

print(cnt)