matrix_a = []
for i in range(3):
    row = list(map(int, input().split()))
    matrix_a.append(row)

input()

matrix_b = []
for i in range(3):
    row = list(map(int, input().split()))
    matrix_b.append(row)

matrix = [[0 for _ in range(3)] for _ in range(3)]

# 행렬 곱셈 수행
for i in range(3):
    for j in range(3):
        matrix[i][j] += matrix_a[i][j] * matrix_b[i][j]

# 결과 출력
for row in matrix:
    print(*row)