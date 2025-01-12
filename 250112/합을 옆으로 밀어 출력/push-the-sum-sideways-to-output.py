n = int(input())

sum1 = 0

for i in range(n):
    x = input()
    sum1 += int(x)

print(str(sum1)[1:] + str(sum1)[0])