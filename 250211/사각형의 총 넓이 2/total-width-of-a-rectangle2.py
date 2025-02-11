N = int(input())
# 좌표값을 저장할 때 더 큰 범위의 배열 사용
MIN_COORD = -100  # 음수 좌표를 고려한 최소값
MAX_COORD = 100   # 양수 좌표를 고려한 최대값
SIZE = MAX_COORD - MIN_COORD + 1

arr = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    # 좌표를 배열 인덱스로 변환
    x1 = x1 - MIN_COORD
    y1 = y1 - MIN_COORD
    x2 = x2 - MIN_COORD
    y2 = y2 - MIN_COORD
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1

area = 0
for i in range(SIZE):
    for j in range(SIZE):
        if arr[i][j] == 1:
            area += 1

print(area)