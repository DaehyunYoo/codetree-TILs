N = int(input())

def star(n):
    if n == N+1:
        return 
    
    print('*' * n)
    star(n+1)

star(1)