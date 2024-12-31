b, a = map(int, input().split())

answer = []
for i in range(b, a-1, -1):
    if i % 2 != 0:
        answer.append(i)

print(*answer)