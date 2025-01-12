n, A = input().split()
result = 0
for i in range(int(n)):
    x = input()
    if x == A:
        result += 1

print(result)