N, M = map(int, input().split())

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1] # 우, 하, 좌, 상
graph = [[0 for _ in range(M)] for _ in range(N)]

x, y = 0, 0 # Start point

move_dir = 0
new_alpha = 'A'
graph[y][x] = new_alpha

for i in range(2, N*M+1):
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    if nx >= M or nx < 0 or ny < 0 or ny >= N or graph[ny][nx] != 0:
        move_dir = (move_dir + 1) % 4
        nx, ny = x + dxs[move_dir], y + dys[move_dir]
    new_alpha = chr(ord(new_alpha) + 1)
    graph[ny][nx] = new_alpha
    x, y = nx, ny

for i in range(N):
    print(*graph[i])