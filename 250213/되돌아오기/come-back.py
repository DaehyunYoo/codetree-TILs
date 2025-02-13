N = int(input())

dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]  

mapper = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3
}

x, y = 0, 0
positions = [(0, 0)]  # 시작 위치 저장

for _ in range(N):
    w, d = input().split()
    move_dir = mapper[w]
    for _ in range(int(d)):
        x += dxs[move_dir]
        y += dys[move_dir]
        positions.append((x, y))

# (0, 0)이 처음 등장하는 위치 찾기 (시작 위치 제외)
for i in range(1, len(positions)):
    if positions[i] == (0, 0):
        print(i)
        break
else:
    print(-1)