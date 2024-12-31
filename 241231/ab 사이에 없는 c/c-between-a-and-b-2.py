a, b, c = map(int, input().split())

# c의 배수가 존재하는지 확인하는 함수
def has_multiple():
    # a 이상인 첫 번째 c의 배수 찾기
    first_multiple = ((a + c - 1) // c) * c
    
    # 첫 번째 c의 배수가 b 이하인지 확인
    if first_multiple <= b:
        return True
    return False

# 결과 출력 (c의 배수가 없으면 YES, 있으면 NO)
if not has_multiple():
    print("YES")
else:
    print("NO")