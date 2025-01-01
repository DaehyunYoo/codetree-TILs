n = int(input())

for i in range(n):
    stars = n - i
    
    for j in range(stars):
        print('*' * stars, end=" ")
    print()