def solve_tile_problem():
    # 명령의 개수 N 입력
    N = int(input())
    
    # 타일 상태를 저장할 배열 (-1: 회색, 1: 검은색, 0: 초기상태)
    # 충분한 크기의 배열 생성 (왼쪽, 오른쪽 이동 고려)
    tiles = [0] * 2001
    position = 1000  # 중앙에서 시작
    
    # N개의 명령 처리
    for _ in range(N):
        x, direction = input().split()
        x = int(x)
        
        if direction == 'L':
            # 왼쪽으로 이동하면서 회색으로 칠하기
            for i in range(x):
                position -= 1
                tiles[position] = -1
        else:  # direction == 'R'
            # 오른쪽으로 이동하면서 검은색으로 칠하기
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