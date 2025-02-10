OFFSET = 100  # 음수 처리를 위한 오프셋
MAX_R = 200   # 배열 최대 크기

N = int(input())
line = [0 for _ in range(MAX_R + 1)]  # 크기를 201로 변경

for i in range(N):
    x1, x2 = map(int, input().split())
    # OFFSET을 더해서 음수 입력 처리
    x1, x2 = x1 + OFFSET, x2 + OFFSET
    for j in range(x1, x2):  # x2는 포함하지 않음
        line[j] += 1

print(max(line))