N = int(input())
i = 1
while True:
    # i += 1
    if 2**i == N:
        break
        print(i)
    else:
        i+= 1

print(i)