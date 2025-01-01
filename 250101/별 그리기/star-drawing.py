n = int(input())

for i in range(n):
    print(" " * (n-i-1), end="")
    
    for j in range(2*i+1):
        print("*", end="")
    print()

for i in range(n-1, 0, -1):
    print(" " * (n-i), end="")

    for j in range(2*i-1):
        print("*", end="")
    print()