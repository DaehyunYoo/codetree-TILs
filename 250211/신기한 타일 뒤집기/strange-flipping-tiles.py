N = int(input())
line = [0] * 200000
point = 100000

for _ in range(N):
    x, c = input().split()
    x = int(x)
    
    if c == 'L':
        # 현재 위치부터 왼쪽으로 x칸 이동하며 칠하기
        for i in range(x):
            line[point - i] = -1
        point = point - x + 1  # 마지막 위치로 이동
    else:
        # 현재 위치부터 오른쪽으로 x칸 이동하며 칠하기
        for i in range(x):
            line[point + i] = 1
        point = point + x - 1  # 마지막 위치로 이동

# 흰색(-1)과 검은색(1) 타일 개수 계산
white = black = 0
for tile in line:
    if tile == -1:
        white += 1
    elif tile == 1:
        black += 1

print(white, black)