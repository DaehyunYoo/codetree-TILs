N = int(input())

line = [0 for _ in range(202)]  # 이동 경로를 기록할 배열
point = 100  

for i in range(N):
    cnt, direction = input().split()
    cnt = int(cnt)  
    
    if direction == 'R':
        for j in range(cnt):
            line[point + j] += 1  # 현재 위치부터 이동 거리만큼 카운트 증가
        point += cnt  # 최종 위치 업데이트
    else:  # direction == 'L'
        for j in range(cnt):
            line[point - j - 1] += 1  # 현재 위치부터 왼쪽으로 이동하며 카운트 증가
        point -= cnt  # 최종 위치 업데이트


result = 0
for i in line:
    if i >= 2:
        result += 1

print(result)