n = int(input())

print('* ' * n)

for i in range(1, n):
    
    print('* ' * i)

    print('* ' * (n - i))

print('* ' * n)