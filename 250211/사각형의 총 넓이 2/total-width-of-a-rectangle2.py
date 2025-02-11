N = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)]  # 좌표 범위에 맞게 조정

# 직사각형 표시
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    # 주의: x는 행을, y는 열을 나타내도록 수정
    for i in range(x1, x2):  # x2는 포함하지 않음
        for j in range(y1, y2):  # y2는 포함하지 않음
            arr[i][j] = 1

# 면적 계산
area = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            area += 1

print(area)