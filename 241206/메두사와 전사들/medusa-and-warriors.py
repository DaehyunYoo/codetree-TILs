import sys
from collections import deque
from typing import List, Tuple

# 전역 상수 정의
INF = int(1e9) + 10  # 무한대를 나타내는 상수
DX = [-1, 1, 0, 0]  # 방향 배열: 위, 아래, 왼쪽, 오른쪽
DY = [0, 0, -1, 1]

def compute_distances(start_x: int, start_y: int, N: int, obstacle_grid: List[List[int]]) -> List[List[int]]:
    """BFS를 이용하여 종료 지점에서 모든 도달 가능한 셀까지의 최단 거리를 계산하는 함수"""
    distance_grid = [[INF if obstacle_grid[i][j] else -1 for j in range(N)] for i in range(N)]
    queue = deque()
    queue.append((start_x, start_y))
    distance_grid[start_x][start_y] = 0

    while queue:
        current_x, current_y = queue.popleft()
        for dir in range(4):
            next_x = current_x + DX[dir]
            next_y = current_y + DY[dir]
            if next_x < 0 or next_y < 0 or next_x >= N or next_y >= N:
                continue
            if distance_grid[next_x][next_y] != -1:
                continue
            distance_grid[next_x][next_y] = distance_grid[current_x][current_y] + 1
            queue.append((next_x, next_y))
    
    return distance_grid

# 입력 처리
input = sys.stdin.read
data = input().split()
idx = 0

N = int(data[idx]); idx += 1  # 그리드 크기
M = int(data[idx]); idx += 1  # 전사 수

start_x = int(data[idx]); idx += 1
start_y = int(data[idx]); idx += 1
end_x = int(data[idx]); idx += 1
end_y = int(data[idx]); idx += 1

# 초기 전사 위치 입력
warrior_positions = []
for _ in range(M):
    x = int(data[idx]); idx += 1
    y = int(data[idx]); idx += 1
    warrior_positions.append([x, y])  # 튜플 대신 리스트 사용

# 장애물 그리드 입력
obstacle_grid = []
for _ in range(N):
    row = []
    for _ in range(N):
        cell = int(data[idx]); idx += 1
        row.append(cell)
    obstacle_grid.append(row)

# 시작/종료 지점 장애물 체크
assert obstacle_grid[start_x][start_y] == 0, "시작 지점에 장애물이 있습니다."
assert obstacle_grid[end_x][end_y] == 0, "종료 지점에 장애물이 있습니다."

# 거리 그리드 계산
distance_grid = compute_distances(end_x, end_y, N, obstacle_grid)

# 도달 불가능 체크
if distance_grid[start_x][start_y] == -1:
    print("-1")
    sys.exit()

current_x, current_y = start_x, start_y
sight_map = [[0 for _ in range(N)] for _ in range(N)]
warrior_count_grid = [[0 for _ in range(N)] for _ in range(N)]

# 초기 전사 수 그리드 설정
for pos in warrior_positions:
    if pos[0] != -1:  # 잡히지 않은 전사만 카운트
        warrior_count_grid[pos[0]][pos[1]] += 1

# 메인 게임 루프
while True:
    moved = False

    # 플레이어 이동
    for dir in range(4):
        next_x = current_x + DX[dir]
        next_y = current_y + DY[dir]
        if next_x < 0 or next_y < 0 or next_x >= N or next_y >= N:
            continue
        if distance_grid[next_x][next_y] < distance_grid[current_x][current_y]:
            current_x, current_y = next_x, next_y
            moved = True
            break

    # 종료 조건 체크
    if current_x == end_x and current_y == end_y:
        print("0")
        break

    # 현재 위치의 전사 제거
    for i in range(M):
        if warrior_positions[i][0] == current_x and warrior_positions[i][1] == current_y:
            warrior_positions[i] = [-1, -1]

    # 전사 수 그리드 업데이트
    warrior_count_grid = [[0 for _ in range(N)] for _ in range(N)]
    for pos in warrior_positions:
        if pos[0] != -1:
            warrior_count_grid[pos[0]][pos[1]] += 1

    # 시야 맵 초기화
    sight_map = [[0 for _ in range(N)] for _ in range(N)]
    
    # 최적의 시야 방향 선택
    max_coverage = -1
    best_direction = -1
    
    # 각 방향에 대한 시야 테스트
    for test_dir in range(4):
        test_sight_map = [[0 for _ in range(N)] for _ in range(N)]
        coverage = 0
        
        if test_dir == 0:  # 위쪽
            for i in range(current_x - 1, -1, -1):
                left = max(0, current_y - (current_x - i))
                right = min(N - 1, current_y + (current_x - i))
                for j in range(left, right + 1):
                    test_sight_map[i][j] = 1
                    coverage += warrior_count_grid[i][j]
                
        elif test_dir == 1:  # 아래쪽
            for i in range(current_x + 1, N):
                left = max(0, current_y - (i - current_x))
                right = min(N - 1, current_y + (i - current_x))
                for j in range(left, right + 1):
                    test_sight_map[i][j] = 1
                    coverage += warrior_count_grid[i][j]
                    
        elif test_dir == 2:  # 왼쪽
            for j in range(current_y - 1, -1, -1):
                top = max(0, current_x - (current_y - j))
                bottom = min(N - 1, current_x + (current_y - j))
                for i in range(top, bottom + 1):
                    test_sight_map[i][j] = 1
                    coverage += warrior_count_grid[i][j]
                    
        else:  # 오른쪽
            for j in range(current_y + 1, N):
                top = max(0, current_x - (j - current_y))
                bottom = min(N - 1, current_x + (j - current_y))
                for i in range(top, bottom + 1):
                    test_sight_map[i][j] = 1
                    coverage += warrior_count_grid[i][j]
        
        if coverage > max_coverage:
            max_coverage = coverage
            best_direction = test_dir
            sight_map = [row[:] for row in test_sight_map]

    # 전사 이동 및 충돌 처리
    warriors_moved = 0
    warriors_hit = 0
    
    for i in range(M):
        if warrior_positions[i][0] == -1:
            continue
            
        warrior_x, warrior_y = warrior_positions[i]
        if sight_map[warrior_x][warrior_y]:
            continue

        current_distance = abs(current_x - warrior_x) + abs(current_y - warrior_y)
        has_moved = False

        # 첫 번째 이동
        for dir in range(4):
            next_x = warrior_x + DX[dir]
            next_y = warrior_y + DY[dir]
            
            if next_x < 0 or next_y < 0 or next_x >= N or next_y >= N:
                continue
            if sight_map[next_x][next_y]:
                continue
                
            new_distance = abs(current_x - next_x) + abs(current_y - next_y)
            if new_distance < current_distance:
                warrior_x, warrior_y = next_x, next_y
                has_moved = True
                warriors_moved += 1
                break

        # 두 번째 이동
        if has_moved:
            new_distance = abs(current_x - warrior_x) + abs(current_y - warrior_y)
            for dir in range(4):
                opposite_dir = (dir + 2) % 4
                next_x = warrior_x + DX[opposite_dir]
                next_y = warrior_y + DY[opposite_dir]
                
                if next_x < 0 or next_y < 0 or next_x >= N or next_y >= N:
                    continue
                if sight_map[next_x][next_y]:
                    continue
                    
                further_distance = abs(current_x - next_x) + abs(current_y - next_y)
                if further_distance < new_distance:
                    warrior_x, warrior_y = next_x, next_y
                    warriors_moved += 1
                    break

        warrior_positions[i] = [warrior_x, warrior_y]

    # 플레이어와 충돌한 전사 처리
    for i in range(M):
        if warrior_positions[i][0] == -1:
            continue
        if warrior_positions[i][0] == current_x and warrior_positions[i][1] == current_y:
            warriors_hit += 1
            warrior_positions[i] = [-1, -1]

    # 결과 출력
    print(f"{warriors_moved} {max_coverage} {warriors_hit}")