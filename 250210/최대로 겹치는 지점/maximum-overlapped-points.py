N = int(input())
line = [0 for _ in range(101)]

for i in range(N):
    x1, x2 = map(int, input().split())
    for j in range(x1-1, x2):
        line[j] += 1

print(max(line))
