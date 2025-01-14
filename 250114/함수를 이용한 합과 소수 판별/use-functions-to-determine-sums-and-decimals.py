a, b = map(int, input().split())
cnt = 0

def func1(x):
    # 2보다 작은 수는 소수가 아님
    if x < 2:
        return False
    
    # 2는 소수
    if x == 2:
        return True
    
    # 2를 제외한 짝수는 소수가 아님
    if x % 2 == 0:
        return False
    
    # 제곱근까지만 홀수로 나누어 확인
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

def func2(x):
    str_x = str(x)
    suma = 0
    for i in str_x:
        suma += int(i)
    if suma % 2 == 0:
        return True
    return False

for i in range(a, b+1):
    if func1(i) and func2(i):
        cnt += 1

print(cnt)