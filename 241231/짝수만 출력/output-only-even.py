a, b = map(int, input().split())

answer = []
while b >= a:
    if a % 2 == 0:
        answer.append(a)
    a += 1
print(*answer)