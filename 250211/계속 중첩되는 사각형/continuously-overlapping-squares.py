N = int(input())

min_coord = -100
max_coord = 100
size = max_coord - min_coord + 1
arr = [[0 for _ in range(size)] for _ in range(size)]

for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    if i % 2 == 0: # 빨간색
        for j in range(x1, x2):
            for k in range(y1, y2):
                arr[j][k] = 1
    else:
        for j in range(x1, x2):
            for k in range(y1, y2):
                arr[j][k] = 2

result = 0
for i in range(len(arr)):
    result += arr[i].count(2)

print(result)