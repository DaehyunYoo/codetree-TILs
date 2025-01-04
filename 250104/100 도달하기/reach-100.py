n = int(input())

a, b = 1, n
print(a, b, end=" ")

for i in range(3, 10^9):
    a, b = b, a+b
    if b > 100:
        print(b, end=" ")
        break
    else:
        print(b, end=" ")