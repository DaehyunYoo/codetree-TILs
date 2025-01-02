n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or (i == 1 and j == 1) or i == j:
            print('*', end=" ")
        else:
            if i < j:
                print(" ", end=" ")
            else:
                print('*', end=' ')
    print()