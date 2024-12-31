a, b, c = map(int, input().split())

# a 이상인 첫 번째 c의 배수 찾기
first_multiple = ((a + c - 1) // c) * c

# 첫 번째 c의 배수가 b 이하인지 확인
if first_multiple <= b:
    print("YES")
else:
    print("NO")