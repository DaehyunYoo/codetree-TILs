A = input()
sum = 0
for i in A:
    if i.isdigit():
        sum += int(i)

print(sum)