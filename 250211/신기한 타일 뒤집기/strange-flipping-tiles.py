N = int(input())
line = [0] * 200000  # 배열 크기를 크게 증가
point = 100000       # 중앙점도 그에 맞게 조정

for _ in range(N):
    x, c = input().split()
    x = int(x)
    
    if c == 'L':
        # 현재 위치에서 왼쪽으로 x만큼 칠하기
        for i in range(point, point - x, -1):
            line[i] = -1
        point = point - x  # 마지막 위치로 이동
    else:
        # 현재 위치에서 오른쪽으로 x만큼 칠하기
        for i in range(point, point + x):
            line[i] = 1
        point = point + x - 1  # 마지막 위치로 이동

# 흰색(-1)과 검은색(1) 타일 개수 계산
white = 0
black = 0
for tile in line:
    if tile == -1:
        white += 1
    elif tile == 1:
        black += 1

print(white, black)