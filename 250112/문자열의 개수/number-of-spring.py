cnt = 0
result = []
num = 1

while True:
    x = input()
    if x == '0':
        break
    else:
        cnt += 1
        result.append(x)

print(cnt)
for i in range(len(result)):
    if i % 2 == 0:
        print(result[i])