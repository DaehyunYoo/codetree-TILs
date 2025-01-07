n, m = map(int, input().split())
arr = 0
matrix = [[0 for _ in range(m)] for _ in range(n)]
# 열을 기준으로 순회
for i in range(m):
    # 짝수 열일 경우 위에서 아래로
    if i % 2 == 0:
        for j in range(n):
            matrix[j][i] = arr
            arr += 1
    # 홀수 열일 경우 아래에서 위로
    else:
        for j in range(n-1, -1, -1):
            matrix[j][i] = arr
            arr += 1

# 결과 출력
for i in range(n):
    print(*matrix[i])