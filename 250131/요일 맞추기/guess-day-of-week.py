m1, d1, m2, d2 = map(int, input().split())

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

days = 0

reverse = False

while True:
    if m1 == m2 and d1 == d2:
        break

    if (m1 == m2 and d1 > d2) or (m1 > m2):
        reverse = True
        if d1 == 1:
            days += 1
            d1 = month_days[m1-1]
            m1 -= 1
        d1 -= 1
        days += 1
    
    else:
        if d1 == month_days[m1]:
            d1 = 1
            days += 1
            m1 += 1
        
        d1 += 1
        days += 1

result = days % 7

if reverse:
    print(day_of_week[-result + 7])
else:
    print(day_of_week[result])
