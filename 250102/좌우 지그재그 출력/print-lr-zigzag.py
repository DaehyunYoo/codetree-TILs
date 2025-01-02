n = int(input())
cnt = 1
for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            print(i*n + j+1, end=" ")
    else:
        for j in range(n):
            print(i*n + n - j, end=" ")
    print()