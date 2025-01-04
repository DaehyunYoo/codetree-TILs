n = int(input())

print(n, end=" ")
for i in range(2, 11):
    if (n * i) % 5 == 0 and (n * i-1) % 5 == 0:
        print(n * i, end=" ")
        break
    print(n * i, end=" ")