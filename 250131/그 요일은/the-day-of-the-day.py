m1, d1, m2, d2 = map(int, input().split())
A = input()

month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
days = 0

while True:
    if m1 == m2 and d1 == d2:
        break
    
    if d1 == month_days[m1]:
        d1 = 1
        m1 += 1
        days += 1
    d1 += 1
    days += 1

target_day_idx = day_of_week.index(A)
count = 0

for i in range(days + 1):
    if i % 7 == target_day_idx:
        count += 1

print(count)