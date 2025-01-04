# 첫 번째 줄에서 두 정수 입력받기 (공백으로 구분)
a, b = map(int, input().split())

# 첫 번째 두 수 출력
print(a, b, end=' ')

# 8개의 피보나치 수 추가로 출력
for _ in range(8):
    # 다음 피보나치 수 계산
    next_num = a + b
    if next_num > 10:
        print(next_num % 10, end=" ")
    else:
        print(next_num, end=' ')
    # a, b 값 업데이트
    a = b
    b = next_num