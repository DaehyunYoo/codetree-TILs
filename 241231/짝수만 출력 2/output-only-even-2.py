b, a = map(int, input().split())

answer = []
while b >= a:
    if b % 2 == 0:
        answer.append(b)
    b -= 1

print(*answer)