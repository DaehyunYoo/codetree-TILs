n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
num = 1

# 첫 번째 반은 첫 번째 행에서 시작하는 대각선들
for start_j in range(m):
    i, j = 0, start_j
    while i < n and j >= 0:
        matrix[i][j] = num
        num += 1
        i += 1
        j -= 1

# 두 번째 반은 마지막 열에서 시작하는 대각선들
for start_i in range(1, n):
    i, j = start_i, m-1
    while i < n and j >= 0:
        matrix[i][j] = num
        num += 1
        i += 1
        j -= 1

# 결과 출력
for row in matrix:
    print(*row)