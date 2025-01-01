n = int(input())

for i in range(n):
    print('*' * (i+1))
    print('')

for j in range(n-1, 0, -1):
    print('*'*j)
    print('')