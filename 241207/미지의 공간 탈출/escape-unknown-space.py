import sys
from collections import deque

input = sys.stdin.readline

MAXN = 20
MAXM = 20
MAXF = 400
MAXP = MAXF*6
INF = int(1e9+10)

N, M, E = map(int, input().split())

# 공간의 평면도
SpaceMap = [list(map(int, input().split())) for _ in range(N)]

# 시간의 벽 단면도: 동(0), 서(2), 남(1), 북(3), 위(4) 순으로 입력
TimeWall = [[[0]*(M) for _ in range(M)] for _ in range(5)]

# 동쪽 단면도
for i in range(M):
    TimeWall[0][i] = list(map(int, input().split()))
# 서쪽 단면도
for i in range(M):
    TimeWall[2][i] = list(map(int, input().split()))
# 남쪽 단면도
for i in range(M):
    TimeWall[1][i] = list(map(int, input().split()))
# 북쪽 단면도
for i in range(M):
    TimeWall[3][i] = list(map(int, input().split()))
# 위쪽 단면도
for i in range(M):
    TimeWall[4][i] = list(map(int, input().split()))

# 시간 이상 현상 정보 (xpos, ypos, direction, cycle, alive)
events = [[0,0,0,0,0] for _ in range(MAXF+10)]
for i in range(1, E+1):
    x, y, d, c = map(int, input().split())
    # 방향 보정 (문제 특정 조건)
    if d == 1:
        d = 2
    elif d == 2:
        d = 1
    events[i] = [x, y, d, c, 1]

# 그래프 구성용 배열
SpaceMapCellId = [[0]*(N+10) for _ in range(N+10)]
TimeWallCellId = [[[0]*(M+10) for _ in range(M+10)] for _ in range(6)]

def build_graph(N, M):
    # 그래프를 인접 리스트 형태로 만들기 위한 준비
    # 방향 순서: 동(0), 남(1), 서(2), 북(3)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cnt = 0

    # 평면도의 셀에 번호 부여
    for i in range(N):
        for j in range(N):
            if SpaceMap[i][j] != 3:
                cnt += 1
                SpaceMapCellId[i][j] = cnt

    # 단면도의 셀에 번호 부여 (동->남->서->북->위)
    # 동(0), 남(1), 서(2), 북(3), 위(4)
    for t in range(5):
        for i in range(M):
            for j in range(M):
                cnt += 1
                TimeWallCellId[t][i][j] = cnt

    # 그래프 초기화: cnt개의 정점, 각 정점마다 4방향 인접 리스트
    Graph = [[-1]*4 for _ in range(cnt+1)]

    # 평면도 인접한 셀 연결
    for i in range(N):
        for j in range(N):
            if SpaceMap[i][j] != 3:
                idx = SpaceMapCellId[i][j]
                for dd in range(4):
                    nx, ny = i+dx[dd], j+dy[dd]
                    if 0 <= nx < N and 0 <= ny < N:
                        if SpaceMap[nx][ny] != 3:
                            Graph[idx][dd] = SpaceMapCellId[nx][ny]

    # 단면도 연결 (동,남,서,북)
    # 동(0), 남(1), 서(2), 북(3)의 경우 원통형으로 연결됨
    for t in range(4):
        for i in range(M):
            for j in range(M):
                idx = TimeWallCellId[t][i][j]
                for dd in range(4):
                    nx, ny = i+dx[dd], j+dy[dd]
                    if nx < 0 or nx >= M:
                        continue
                    if ny < 0:
                        # 왼쪽 범위 넘어가면 (t+1)%4 단면도의 맨 오른쪽 열
                        Graph[idx][dd] = TimeWallCellId[(t+1)%4][nx][M-1]
                    elif ny >= M:
                        # 오른쪽 범위 넘어가면 (t+3)%4 단면도의 맨 왼쪽 열
                        Graph[idx][dd] = TimeWallCellId[(t+3)%4][nx][0]
                    else:
                        Graph[idx][dd] = TimeWallCellId[t][nx][ny]

    # 위쪽 단면도(4) 연결
    for i in range(M):
        for j in range(M):
            idx = TimeWallCellId[4][i][j]
            for dd in range(4):
                nx, ny = i+dx[dd], j+dy[dd]
                if 0 <= nx < M and 0 <= ny < M:
                    Graph[idx][dd] = TimeWallCellId[4][nx][ny]

    # 위쪽 단면도와 동(0), 남(1), 서(2), 북(3) 단면도 연결
    # 동쪽 단면도와 위쪽 단면도 연결
    for i in range(M):
        idx = TimeWallCellId[4][i][M-1]
        idy = TimeWallCellId[0][0][M-1 - i]
        Graph[idx][0] = idy
        Graph[idy][3] = idx
    # 남쪽 단면도
    for i in range(M):
        idx = TimeWallCellId[4][M-1][i]
        idy = TimeWallCellId[1][0][i]
        Graph[idx][1] = idy
        Graph[idy][3] = idx
    # 서쪽 단면도
    for i in range(M):
        idx = TimeWallCellId[4][i][0]
        idy = TimeWallCellId[2][0][i]
        Graph[idx][2] = idy
        Graph[idy][3] = idx
    # 북쪽 단면도
    for i in range(M):
        idx = TimeWallCellId[4][0][i]
        idy = TimeWallCellId[3][0][M-1 - i]
        Graph[idx][3] = idy
        Graph[idy][3] = idx

    # 평면도에서 시간의 벽 시작점 탐색
    timewallStartx, timewallStarty = -1, -1
    for i in range(N):
        for j in range(N):
            if SpaceMap[i][j] == 3:
                timewallStartx, timewallStarty = i, j
                break
        if timewallStartx != -1:
            break

    # 평면도와 단면도 연결
    # 동쪽 단면도
    if timewallStarty + M < N:
        for i in range(M):
            idx = TimeWallCellId[0][M-1][i]
            idy = SpaceMapCellId[timewallStartx + (M-1 - i)][timewallStarty + M]
            Graph[idx][1] = idy
            Graph[idy][2] = idx
    # 남쪽 단면도
    if timewallStartx + M < N:
        for i in range(M):
            idx = TimeWallCellId[1][M-1][i]
            idy = SpaceMapCellId[timewallStartx + M][timewallStarty + i]
            Graph[idx][1] = idy
            Graph[idy][3] = idx
    # 서쪽 단면도
    if timewallStarty > 0:
        for i in range(M):
            idx = TimeWallCellId[2][M-1][i]
            idy = SpaceMapCellId[timewallStartx + i][timewallStarty - 1]
            Graph[idx][1] = idy
            Graph[idy][0] = idx
    # 북쪽 단면도
    if timewallStartx > 0:
        for i in range(M):
            idx = TimeWallCellId[3][M-1][i]
            idy = SpaceMapCellId[timewallStartx - 1][timewallStarty + (M -1 - i)]
            Graph[idx][1] = idy
            Graph[idy][1] = idx

    return Graph, cnt

Graph, cnt = build_graph(N, M)

dist = [-1]*(cnt+1)

# 장애물, 이벤트 시작점 셀은 도달 불가능 처리
for i in range(N):
    for j in range(N):
        if SpaceMap[i][j] == 3:
            continue
        if SpaceMap[i][j] == 1:
            dist[SpaceMapCellId[i][j]] = INF

for i in range(1, E+1):
    x, y, _, _, alive = events[i]
    if alive:
        dist[SpaceMapCellId[x][y]] = INF

for t in range(5):
    for i in range(M):
        for j in range(M):
            if TimeWall[t][i][j] == 1:
                dist[TimeWallCellId[t][i][j]] = INF

# 출구 위치 탐색
cell_end = -1
for i in range(N):
    for j in range(N):
        if SpaceMap[i][j] == 4:
            cell_end = SpaceMapCellId[i][j]
            break
    if cell_end != -1:
        break

# 타임머신 시작점 (위쪽 단면도에서 2)
cell_start = -1
for i in range(M):
    for j in range(M):
        if TimeWall[4][i][j] == 2:
            cell_start = TimeWallCellId[4][i][j]
            break
    if cell_start != -1:
        break

# BFS 함수 구현
def bfs():
    dist[cell_start] = 0
    que = deque([cell_start])
    runs = 1

    # 이벤트 방향에 따른 dx, dy
    # 0: 동, 1: 남, 2: 서, 3: 북
    # events[i][2]에 저장된 방향 값에 따른 이동
    event_dx = [0,1,0,-1]
    event_dy = [1,0,-1,0]

    while True:
        # 이상 현상 확장 처리
        for i in range(1, E+1):
            if events[i][4] == 0:  # alive == 0
                continue
            if runs % events[i][3] != 0:  # cycle
                continue
            ex, ey, ed, ec, ea = events[i]
            steps = runs // ec
            nx = ex + event_dx[ed]*steps
            ny = ey + event_dy[ed]*steps
            if nx<0 or ny<0 or nx>=N or ny>=N:
                events[i][4] = 0
                continue
            if SpaceMap[nx][ny] != 0: 
                # 장애물 등 만났으니 이벤트 종료
                events[i][4] = 0
                continue
            idx = SpaceMapCellId[nx][ny]
            dist[idx] = INF

        next_cells = []
        size = len(que)
        for _ in range(size):
            idx = que.popleft()
            for d in range(4):
                idy = Graph[idx][d]
                if idy == -1:
                    continue
                if dist[idy] != -1:
                    continue
                dist[idy] = runs
                next_cells.append(idy)

        if not next_cells:
            break
        que.extend(next_cells)
        if dist[cell_end] != -1:
            break
        runs += 1

    return dist[cell_end]

ans = bfs()

if ans == -1 or ans >= INF:
    print(-1)
else:
    print(ans)