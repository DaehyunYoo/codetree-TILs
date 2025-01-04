n = int(input())
cnt = 0
for i in range(n):
    scores = list(map(int, input().split()))
    total = sum(scores)
    average = total / 4
    if average >= 60:
        cnt += 1
        print('pass')
    else:
        print('fail')
print(cnt)