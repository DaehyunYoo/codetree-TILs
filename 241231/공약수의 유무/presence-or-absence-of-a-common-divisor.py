# a, b 입력받기
a, b = map(int, input().split())

# 최대공약수를 구하는 함수
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# 주어진 수 n의 약수들을 구하는 함수
def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n//i:  # 제곱근이 아닌 경우 대응되는 약수도 추가
                divisors.append(n//i)
    return sorted(divisors)

# 1920과 2880의 최대공약수 구하기
gcd_num = gcd(1920, 2880)

# 최대공약수의 약수들 구하기
divisors = get_divisors(gcd_num)

# a이상 b이하 범위에 약수가 있는지 확인
exists = False
for d in divisors:
    if a <= d <= b:
        exists = True
        break

# 결과 출력
print(1 if exists else 0)