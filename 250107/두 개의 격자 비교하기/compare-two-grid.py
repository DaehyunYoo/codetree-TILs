n, m = map(int, input().split())

matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

matrix2 = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix2.append(row)

result = [[0 for i in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if matrix[i][j] != matrix2[i][j]:
            result[i][j] += 1

for i in range(n):
    print(*result[i])