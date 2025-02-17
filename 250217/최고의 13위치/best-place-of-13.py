N = int(input())

coins = []
for _ in range(N):
    coins.append(list(map(int, input().split())))

max_cnt = 0
for i in range(N):
    for j in range(N-2):
        cnt = 0
        if coins[i][j] == 1:
            cnt += 1
        if coins[i][j+1] == 1:
            cnt += 1
        if coins[i][j+2] == 1:
            cnt += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)