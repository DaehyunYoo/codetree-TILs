n = int(input())

# 합성수인지 판별하는 함수
def is_composite():
    # 2부터 n-1까지 순회
    for i in range(2, n):
        # n이 i로 나누어떨어지면 합성수
        if n % i == 0:
            return True
    return False

# 결과 출력
if is_composite():
    print("C")
else:
    print("N")