n = int(input())
cnt, sum, mean = 0, 0, 0
for i in range(n):
    num = int(input())
    sum += num
    cnt += 1

if sum != 0:
    mean = sum / cnt
    print(sum, f'{mean:.1f}')
else:
    print(0, 0.0)