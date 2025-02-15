N, M = map(int, input().split())

graph = [[0 for _ in range(M)] for _ in range(N)]

x, y = 0, 0 # Start point
direction = 0 # Start Direction

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1] # 하, 우, 상, 좌
graph[x][y] = 1

for i in range(2, N*M+1):
    nx, ny = x + dxs[direction], y + dys[direction]
    if nx < 0 or nx >= N or ny < 0 or ny >= M or graph[nx][ny] != 0:
        # 방향 전환
        direction = (direction + 1) % 4
        nx = x + dxs[direction]
        ny = y + dys[direction]
    
    graph[nx][ny] = i
    x, y = nx, ny

for i in range(N):
    print(*graph[i])
