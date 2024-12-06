import sys
from collections import deque
input = sys.stdin.readline

# 마을의 크기(N)와 전사의 수(M)
N, M = map(int, input().split())

# 메두사의 집 위치(sr, sc)와 공원 위치(er, ec)
sr, sc, er, ec = map(int, input().split())

# M명의 전사들의 좌표
warriors = []
if M > 0:  # 전사가 있는 경우에만 입력 받기
    warrior_positions = list(map(int, input().split()))
    for i in range(0, len(warrior_positions), 2):
        warriors.append((warrior_positions[i], warrior_positions[i+1]))

# N x N 크기의 마을 도로 정보
road = [list(map(int, input().split())) for _ in range(N)]

# 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1. 공원에서 출발하는 BFS로 모든 지점까지의 최단 거리 계산
# 메두사는 이 정보를 이용해 매 턴 공원으로 가는 최단 경로를 따라간다.
dist_to_park = [[-1]*N for _ in range(N)]
queue = deque()
if road[er][ec] == 0:
    dist_to_park[er][ec] = 0
    queue.append((er, ec))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and road[nx][ny] == 0 and dist_to_park[nx][ny] == -1:
            dist_to_park[nx][ny] = dist_to_park[x][y] + 1
            queue.append((nx, ny))

# 만약 메두사의 초기 위치에서 공원까지 갈 수 없다면, 바로 종료
if dist_to_park[sr][sc] == -1:
    print(-1)
    sys.exit(0)

medusa_x, medusa_y = sr, sc

def manhatten_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# 시야 범위 계산을 개선: 방향별로 삼각형 형태를 효율적으로 탐색
# 동시에 warrior에 의한 가림 처리도 여기서 수행
def get_sight_and_blocked(medusa_x, medusa_y, warriors):
    # warriors를 집합으로 관리하여 빠른 조회
    warrior_set = set(warriors)

    # direction별 시야 계산 로직
    # 상(0): 위쪽으로 i칸 이동 시 y축 범위: medusa_y - i ~ medusa_y + i
    # 하(1): 아래쪽
    # 좌(2): 왼쪽
    # 우(3): 오른쪽

    def sight_in_direction(direction):
        visible = set()
        # direction에 따라 medusa_x, medusa_y에서부터 확장
        if direction == 0:  # 상
            for d in range(1, medusa_x+1):
                row = medusa_x - d
                start_col = medusa_y - d
                end_col = medusa_y + d
                if start_col < 0: start_col = 0
                if end_col >= N: end_col = N-1

                line_blocked = False
                for col in range(start_col, end_col+1):
                    if road[row][col] == 0:
                        visible.add((row, col))
                        if (row, col) in warrior_set:
                            # 전사를 만났으므로 이 라인 뒤는 가려짐, 다음 칸부터 안 봄
                            line_blocked = True
                    # 전사를 만난 이후는 추가하지 않음
                if line_blocked:
                    # 한 줄에서 전사 만났으면 그 뒤로 계속 진행 (위쪽 방향) 가능하지만
                    # 전사는 한 줄에서만 가림. 다른 줄은 계속 볼 수 있음.
                    pass

        elif direction == 1:  # 하
            for d in range(1, N - medusa_x):
                row = medusa_x + d
                start_col = medusa_y - d
                end_col = medusa_y + d
                if start_col < 0: start_col = 0
                if end_col >= N: end_col = N-1

                line_blocked = False
                for col in range(start_col, end_col+1):
                    if road[row][col] == 0:
                        visible.add((row, col))
                        if (row, col) in warrior_set:
                            line_blocked = True
                if line_blocked:
                    pass

        elif direction == 2:  # 좌
            for d in range(1, medusa_y+1):
                col = medusa_y - d
                start_row = medusa_x - d
                end_row = medusa_x + d
                if start_row < 0: start_row = 0
                if end_row >= N: end_row = N-1

                line_blocked = False
                for row in range(start_row, end_row+1):
                    if road[row][col] == 0:
                        visible.add((row, col))
                        if (row, col) in warrior_set:
                            line_blocked = True
                if line_blocked:
                    pass

        else:  # 우(3)
            for d in range(1, N - medusa_y):
                col = medusa_y + d
                start_row = medusa_x - d
                end_row = medusa_x + d
                if start_row < 0: start_row = 0
                if end_row >= N: end_row = N-1

                line_blocked = False
                for row in range(start_row, end_row+1):
                    if road[row][col] == 0:
                        visible.add((row, col))
                        if (row, col) in warrior_set:
                            line_blocked = True
                if line_blocked:
                    pass

        return visible

    max_warriors = -1
    best_dir = 0
    best_sight = set()

    # 각 방향에 대해 전사 수를 계산
    for direction in range(4):
        sight = sight_in_direction(direction)
        # sight 내에 있는 전사 수
        visible_warriors = sum(1 for w in warriors if w in sight)
        if visible_warriors > max_warriors:
            max_warriors = visible_warriors
            best_dir = direction
            best_sight = sight

    return best_dir, best_sight

def move_warriors(medusa_x, medusa_y, warriors, sight):
    dxx = [-1, 1, 0, 0]
    dyy = [0, 0, -1, 1]
    new_positions = []
    total_distance = 0

    # 시야 내 전사들은 움직이지 않음
    in_sight = set(w for w in warriors if w in sight)

    for wx, wy in warriors:
        if (wx, wy) in in_sight:
            new_positions.append((wx, wy))
            continue

        # 첫 번째 이동
        min_dist = manhatten_distance(wx, wy, medusa_x, medusa_y)
        best_pos = (wx, wy)
        for i in range(4):
            nx = wx + dxx[i]
            ny = wy + dyy[i]
            if 0 <= nx < N and 0 <= ny < N and road[nx][ny] == 0:
                if (nx, ny) not in sight:
                    new_dist = manhatten_distance(nx, ny, medusa_x, medusa_y)
                    if new_dist < min_dist:
                        min_dist = new_dist
                        best_pos = (nx, ny)
        if best_pos != (wx, wy):
            total_distance += 1

        # 두 번째 이동
        wx2, wy2 = best_pos
        min_dist = manhatten_distance(wx2, wy2, medusa_x, medusa_y)
        second_pos = best_pos
        # 반대 방향 이동 시도 (메두사와의 거리 더 줄이는 방향)
        for i in range(4):
            nx = wx2 + dxx[i]
            ny = wy2 + dyy[i]
            if 0 <= nx < N and 0 <= ny < N and road[nx][ny] == 0:
                if (nx, ny) not in sight:
                    new_dist = manhatten_distance(nx, ny, medusa_x, medusa_y)
                    if new_dist < min_dist:
                        min_dist = new_dist
                        second_pos = (nx, ny)
        if second_pos != best_pos:
            total_distance += 1

        new_positions.append(second_pos)

    return new_positions, total_distance

def check_warrior_attack(medusa_x, medusa_y, warriors):
    attack_count = 0
    survived_warriors = []
    for wx, wy in warriors:
        if wx == medusa_x and wy == medusa_y:
            attack_count += 1
        else:
            survived_warriors.append((wx, wy))
    return attack_count, survived_warriors

def simulate_turn():
    global medusa_x, medusa_y, warriors

    # 메두사 이동 (사전 계산한 dist_to_park 사용)
    current_dist = dist_to_park[medusa_x][medusa_y]
    if current_dist == 0:  # 이미 공원 도착
        print(0)
        return 1

    # 다음 위치를 dist_to_park를 참조하여 한 칸 이동
    moved = False
    for i in range(4):
        nx = medusa_x + dx[i]
        ny = medusa_y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and dist_to_park[nx][ny] == current_dist - 1:
            medusa_x, medusa_y = nx, ny
            moved = True
            break

    if not moved:
        # 이동할 수 없음 -> -1 출력하고 종료
        print(-1)
        return 1

    # 공원 도착 체크
    if medusa_x == er and medusa_y == ec:
        print(0)
        return 1

    # 2. 메두사의 시선 및 전사 확인
    best_dir, sight = get_sight_and_blocked(medusa_x, medusa_y, warriors)

    # 돌이 된 전사 계산
    stone_count = sum(1 for w in warriors if w in sight)
    active_warriors = [(wx, wy) for wx, wy in warriors if (wx, wy) not in sight]

    # 3. 전사들의 이동
    new_positions, move_distance = move_warriors(medusa_x, medusa_y, active_warriors, sight)

    # 4. 전사들의 공격
    attack_count, survived_warriors = check_warrior_attack(medusa_x, medusa_y, new_positions)

    # 결과 출력
    print(move_distance, stone_count, attack_count)

    # 전사 목록 업데이트
    warriors = survived_warriors

    return 0

while True:
    result = simulate_turn()
    if result != 0:
        break