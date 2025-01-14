M, D = map(int, input().split())

def is_month(x, y):
    if not 1 <= x <= 12:
        return False
    
    if x == 2 and not 1 <= y <= 28:
        return False
    
    if y < 1 or y > 31:
        return False

    return True

if is_month(M, D):
    print('Yes')
else:
    print('No')