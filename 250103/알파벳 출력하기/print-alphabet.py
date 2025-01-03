n = int(input())

num = 65
for i in range(n):
    for j in range(i+1):
        print(chr(num), end="")
        if num != 91:
            num+= 1
        else:
            num = 65
    print()