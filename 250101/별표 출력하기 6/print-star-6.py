n = int(input())

for i in range(n):
    print("  " * i, end="")

    for j in range(2*(n-i)-1):
        print("* ", end="")
    print()

for i in range(n-2, -1, -1):
    print("  "* i, end="")

    for j in range(2*(n-i)-1):
        print("* ", end="")
    print()