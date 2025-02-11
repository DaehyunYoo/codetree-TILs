N = int(input())
min_coord = -100
max_coord = 100
size = max_coord - min_coord + 1

arr = [[0 for _ in range(size)] for _ in range(size)]

for _ in range(N):
    x, y = map(int, input().split())
    x = x - min_coord
    y = y - min_coord
    for i in range(x, x+8):
        for j in range(y, y+8):
            arr[i][j] = 1

result = 0
for i in range(len(arr)):
    result += arr[i].count(1)

print(result)