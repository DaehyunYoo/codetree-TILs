a, b = map(int, input().split())

sum_val = 0
cnt = 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:  # 5의 배수 또는 7의 배수
        sum_val += i
        cnt += 1

if cnt != 0:
    mean = sum_val / cnt
    print(sum_val, f"{mean:.1f}")
else:
    print(0, "0.0")