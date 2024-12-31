a, b = map(int, input().split())
answer = []
if a > 0:
    for i in range(b):
        answer.append(str(a))
    print(''.join(answer))
else:
    print(0)