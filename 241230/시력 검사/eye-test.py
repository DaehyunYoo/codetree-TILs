# 양쪽 눈의 시력 입력 받기
a = float(input())
b = float(input())

# 시력 분류
if a >= 1.0 and b >= 1.0:
    print("High")
elif a >= 0.5 and b >= 0.5:
    print("Middle")
else:
    print("Low")