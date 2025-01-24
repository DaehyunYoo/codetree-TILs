n = int(input())

a = list(map(int, input().split()))

maximum = 0
def f(n):
    if maximum > n:
        return maximum
    else:
        return n

for i in a:
    maximum = f(i)

print(maximum)
