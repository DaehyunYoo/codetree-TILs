N = int(input())
line = [0] * 2000  # 충분한 크기의 배열 생성
point = 1000       # 시작점을 중앙으로 설정

for _ in range(N):
    x, c = input().split()
    x = int(x)
    
    if c == 'L':  # 왼쪽으로 이동
        for i in range(x):
            line[point - i] = -1  # 현재 위치부터 왼쪽으로 이동하며 -1 표시
        point -= (x - 1)  # 마지막 위치로 이동
    else:  # 오른쪽으로 이동
        for i in range(x):
            line[point + i] = 1   # 현재 위치부터 오른쪽으로 이동하며 1 표시
        point += (x - 1)  # 마지막 위치로 이동

# 흰색(-1)과 검은색(1) 타일 개수 계산
white = 0
black = 0
for tile in line:
    if tile == -1:
        white += 1
    elif tile == 1:
        black += 1

print(white, black)