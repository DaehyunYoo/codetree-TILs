def calculate_and_modify(x, y):
    # 입력 범위 및 조건 체크
    if not (1 <= x <= 200 and 1 <= y <= 200):
        return None  # 범위를 벗어난 경우
    if x == y:
        return None  # 두 수가 같은 경우
    
    # 작은 수에는 2를 곱하고, 큰 수에는 25를 더함
    smaller = min(x, y) * 2
    larger = max(x, y) + 25
    
    return smaller, larger

# 입력 받기
a, b = map(int, input().split())

# 결과 계산 및 출력
result = calculate_and_modify(a, b)
if result:
    print(*result)