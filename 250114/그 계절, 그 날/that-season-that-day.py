Y, M, D = map(int, input().split())

def season(x):
    if 3 <= x <= 5:
        return 'Spring'
    elif 6 <= x <= 8:
        return 'Summer'
    elif 9 <= x <= 11:
        return 'Fall'
    elif x == 12 or 1 <= x <= 2:
        return 'Winter'
    else:
        return False

def is_month(x):
    if x % 4 == 0 and x % 100 == 0 and x % 400 == 0:
        return True
    if x % 4 == 0 and not x % 100 == 0:
        return True
    if x % 4 == 0:
        return True
    return False

def check_date(x, y, z):
    if not (1 <= y <= 12 and 1 <= z <= 31):
        return False
    
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_month(x):
        days_in_month[2] = 29
    
    if z > days_in_month[y]:
        return False
    
    return True

if not check_date(Y, M, D):
    print(-1)
else:
    print(season(M))