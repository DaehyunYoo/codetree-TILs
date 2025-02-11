def solve_tile_problem():
    # 명령의 개수 N 입력
    N = int(input())
    
    # 최대 이동 가능 거리를 고려한 배열 크기 설정
    # N(최대 1000) * x(최대 100) = 100,000
    # 양방향 이동을 고려하여 중앙에서 ±100,000
    # 여유를 두어 300,000 크기로 설정
    tiles = [0] * 300000
    position = 150000  # 중앙에서 시작
    
    # N개의 명령 처리
    for _ in range(N):
        x, direction = input().split()
        x = int(x)
        
        if direction == 'L':
            # 왼쪽으로 이동하면서 회색(-1)으로 칠하기
            for i in range(x):
                position -= 1
                tiles[position] = -1
        else:  # direction == 'R'
            # 오른쪽으로 이동하면서 검은색(1)으로 칠하기
            for i in range(x):
                tiles[position] = 1
                position += 1
    
    # 회색(-1)과 검은색(1) 타일 개수 세기
    gray_count = tiles.count(-1)
    black_count = tiles.count(1)
    
    # 결과 출력
    print(gray_count, black_count)

# 메인 실행
if __name__ == "__main__":
    solve_tile_problem()