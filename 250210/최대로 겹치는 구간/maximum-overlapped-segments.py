N = int(input())
line = [0 for _ in range(1001)]  # 크기를 1001로 변경 (문제 제한이 보통 1000까지)

for i in range(N):
    x1, x2 = map(int, input().split())
    for j in range(x1-1, x2):  # 인덱스 보정
        line[j] += 1

print(max(line))