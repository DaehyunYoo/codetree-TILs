n = int(input())
matrix = [[0] * n for _ in range(n)]
arr = 1

if n % 2 != 0:
    for i in range(n - 1, -1, -1):
        # i가 짝수일 때는 아래에서 위로 채움
        if i % 2 == 0:
            for j in range(n - 1, -1, -1):
                matrix[j][i] = arr
                arr += 1
        # i가 홀수일 때는 위에서 아래로 채움
        else:
            for j in range(n):
                matrix[j][i] = arr
                arr += 1

else:
    for i in range(n - 1, -1, -1):
        # i가 짝수일 때는 아래에서 위로 채움
        if i % 2 != 0:
            for j in range(n - 1, -1, -1):
                matrix[j][i] = arr
                arr += 1
        # i가 홀수일 때는 위에서 아래로 채움
        else:
            for j in range(n):
                matrix[j][i] = arr
                arr += 1


for row in matrix:
    print(*row)