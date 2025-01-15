# a, b = map(int, input().split())

# def cal(x, y):
#     small = min(x, y) * 2
#     larger = max(x, y) + 25
#     return small, larger

# result = cal(a, b)
# print(*result)
def calculate_and_modify(x, y):
    try:
        smaller = min(x, y) * 2
        larger = max(x, y) + 25
        return smaller, larger
    except TypeError:
        return "입력값이 올바르지 않습니다."

# 입력 받기
try:
    a, b = map(int, input().split())
    result = calculate_and_modify(a, b)
    print(*result)
except ValueError:
    print("정수를 입력해주세요.")