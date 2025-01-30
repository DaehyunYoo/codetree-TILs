class Distance:
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index
        # 맨해튼 거리 계산
        self.manhattan = abs(x) + abs(y)

N = int(input())
points = []

# 입력 받기
for i in range(N):
    x, y = map(int, input().split())
    points.append(Distance(x, y, i+1))

# 맨해튼 거리와 인덱스를 기준으로 정렬
points.sort(key=lambda p: (p.manhattan, p.index))

# 결과 출력
for point in points:
    print(point.index)