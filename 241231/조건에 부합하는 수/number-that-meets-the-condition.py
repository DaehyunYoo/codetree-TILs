a = int(input())

answer = []
for i in range(1, a):
    if not i % 2 == 0 and i % 4 != 0:
        answer.append(i)
    elif not (i % 8) % 2 ==0:
        answer.append(i)
    elif not (i % 7) < 4:
        answer.append(i)

print(*answer)