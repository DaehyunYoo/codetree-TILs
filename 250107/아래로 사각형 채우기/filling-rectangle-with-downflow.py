n = int(input())

matrix = [[0 for i in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][j] = n*(j) + (i+1)

for i in range(len(matrix)):
    print(*matrix[i])