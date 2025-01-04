a, b = map(int, input().split())

print(a, b, end=" ")
for i in range(3, 11):
    a, b = b, b + 2*a
    print(b, end=" ")