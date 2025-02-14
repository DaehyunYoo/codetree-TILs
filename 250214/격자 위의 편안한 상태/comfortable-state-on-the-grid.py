N, M = map(int, input().split())

graph = [[0 for _ in range(N)] for _ in range(N)]
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

for _ in range(M):
    r, c = map(int, input().split())
    cnt = 0 # 칠해진 칸을 확인하는 cnt
    x, y = c-1, r-1
    graph[x][y] = 1
    for i in range(4):
        nx, ny = x + dxs[i], y + dys[i]
        if 0 <= nx < N  and 0 <= ny < N and graph[nx][ny] == 1:
            cnt += 1

    # 편안한 상태 확인
    if cnt == 3:
        print(1)
    else:
        print(0)