n, m = map(int, input().split())

A = list(map(int, input().split()))

def count(x, y):
    global A
    sum = 0
    for i in range(x-1, y):
        sum += A[i]
    print(sum)


for _ in range(m):
    a1, a2 = map(int, input().split())
    count(a1, a2)
