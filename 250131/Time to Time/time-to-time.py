a, b, c, d = map(int, input().split())
time = 0
while True:
    if a == c and b == d:
        break
    
    if b == 59:
        a += 1
        b = 0
        time += 1
    else:
        b += 1
        time += 1

print(time)