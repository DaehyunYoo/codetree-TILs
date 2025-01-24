N = list(map(int, input().split()))
new_n = 1
def f(n):
    if n < 10:
        return n
    return f(n // 10) + n % 10

for i in N:
    new_n *= i

print(f(new_n))