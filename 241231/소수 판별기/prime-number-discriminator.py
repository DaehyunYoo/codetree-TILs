n = int(input())

# 소수 판별 함수
def is_prime():
    # n이 2부터 n-1까지의 어떤 수로도 나누어떨어지지 않아야 소수
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# 결과 출력
if is_prime():
    print('P')
else:
    print('C')