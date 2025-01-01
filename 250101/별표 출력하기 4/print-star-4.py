n = int(input())

# 위쪽 삼각형 출력 (n줄부터 1줄까지)
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()

# 아래쪽 삼각형 출력 (2줄부터 n줄까지)
for i in range(2, n + 1):
    for j in range(i):
        print('*', end=' ')
    print()