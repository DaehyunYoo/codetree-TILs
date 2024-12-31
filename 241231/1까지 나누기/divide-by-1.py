n = int(input())
cnt = 0
for i in range(1, n+1):
    if n <= 1:
        break
    else:
        n //= i
        cnt += 1

print(cnt)