# 두 정수 입력 받기
a, b = map(int, input().split())

# 각 조건 확인 및 결과 출력
print(1 if a >= b else 0)  # a가 b보다 같거나 큰가?
print(1 if a > b else 0)   # a가 b보다 큰가?
print(1 if b >= a else 0)  # b가 a보다 같거나 큰가?
print(1 if b > a else 0)   # b가 a보다 큰가?
print(1 if a == b else 0)  # a와 b가 같은가?
print(1 if a != b else 0)  # a와 b가 다른가?