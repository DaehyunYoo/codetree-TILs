# N = int(input())
# graph = [[0 for _ in range(N)] for _ in range(N)]

# x, y = N // 2, N // 2 # start point
# cnt = 1
# dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1] # 우, 상, 좌, 하

# move_len = 1 # 한방향 이동 거리
# move_dir = 0
# graph[y][x] = cnt


# for _ in range(2, N*N+1):
#     nx, ny = x + dxs[move_dir], y + dys[move_dir]
#     if 0 > nx or nx >= N or ny >= N or ny < 0 or graph[ny][nx] != 0:
#         move_dir = (move_dir + 1) % 4
#         nx, ny = x + dxs[move_dir], y + dys[move_dir]
#     cnt += 1
#     graph[ny][nx] = cnt
#     x, y = nx, ny

# for i in range(N):
#     print(*graph[i])
N = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]

x, y = N // 2, N // 2  # start point
cnt = 1
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]  # 우, 상, 좌, 하
move_dir = 0
graph[y][x] = cnt

move_len = 1  # 한 방향으로 이동할 거리
move_cnt = 0  # 현재 방향으로 이동한 횟수
len_cnt = 0   # 같은 거리로 이동한 방향 수

for i in range(2, N*N+1):
    nx = x + dxs[move_dir]
    ny = y + dys[move_dir]
    
    # 범위를 벗어나거나 이미 숫자가 있는 경우
    if 0 > nx or nx >= N or ny >= N or ny < 0 or graph[ny][nx] != 0:
        break
        
    cnt += 1
    graph[ny][nx] = cnt
    x, y = nx, ny
    
    move_cnt += 1  # 현재 방향으로 이동한 횟수 증가
    
    # 현재 방향으로 정해진 거리만큼 이동했다면
    if move_cnt == move_len:
        move_dir = (move_dir + 1) % 4  # 방향 전환
        move_cnt = 0  # 이동 횟수 초기화
        len_cnt += 1  # 같은 거리로 이동한 방향 수 증가
        
        # 두 방향으로 이동을 완료했다면
        if len_cnt == 2:
            move_len += 1  # 이동할 거리 증가
            len_cnt = 0    # 방향 수 초기화

for i in range(N):
    print(*graph[i])