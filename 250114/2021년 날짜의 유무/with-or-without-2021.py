M, D = map(int, input().split())

def is_month(x, y):
    # 월이 1~12 범위를 벗어나면 False
    if not 1 <= x <= 12:
        return False
    
    # 2월은 28일까지
    if x == 2:
        if not 1 <= y <= 28:
            return False
    # 4, 6, 9, 11월은 30일까지
    elif x in [4, 6, 9, 11]:
        if not 1 <= y <= 30:
            return False
    # 나머지 월은 31일까지
    else:
        if not 1 <= y <= 31:
            return False

    return True

if is_month(M, D):
    print('Yes')
else:
    print('No')