n = int(input())

for i in range(1, n + 1):
    pattern = ''
    for j in range(1, n + 1):
        if j % 2 == 1:
            pattern += str(i)
        else:
            opposite = n - i + 1
            pattern += str(opposite)
    print(pattern)