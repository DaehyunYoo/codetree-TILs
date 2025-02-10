N, K = map(int, input().split())

blocks = [0 for _ in range(N)]

for i in range(K):
    a, b = map(int, input().split())
    for j in range(a-1, b):
        blocks[j] += 1

print(max(blocks))

