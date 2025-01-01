n = int(input())

for i in range(n):
    print("  "* (n - i - 1), end="")

    stars = 2 * i + 1
    for j in range(stars):
        print("* ", end="")
    
    print()