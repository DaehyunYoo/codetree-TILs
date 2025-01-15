A = input()

def check(x):
    # set을 사용하여 중복을 제거하고 고유한 문자만 남김
    unique_chars = set(x)
    # 고유 문자가 2개 이상인지 확인
    return len(unique_chars) >= 2

if check(A):
    print('Yes')
else:
    print('No')