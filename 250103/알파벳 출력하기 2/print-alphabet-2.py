N = int(input())
num = 65
for i in range(N):
    print('  '* i, end="")
    for j in range(N-i):
        print(chr(num), end=" ")
        if num != 90:
            num += 1
        else:
            num = 65
    print()