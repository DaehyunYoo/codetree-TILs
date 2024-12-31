cnt, sum, mean = 0, 0, 0

for i in range(10):
    num = int(input())
    if 0 <= num <= 200:
        sum += num
        cnt += 1

if sum != 0:
    mean = sum / cnt
    print(sum, f'{mean:.1f}')
else:
    print(0, 0.0)