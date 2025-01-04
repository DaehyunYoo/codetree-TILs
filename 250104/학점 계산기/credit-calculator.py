n = int(input())
scores = list(input().split())
total = 0
for i in scores:
    total += float(i)

average = (total/n)
print(f"{average:.1f}")

if average >= 4.0:
    print('Perfect')
elif average >= 3.0:
    print('Good')
else:
    print('Poor')
