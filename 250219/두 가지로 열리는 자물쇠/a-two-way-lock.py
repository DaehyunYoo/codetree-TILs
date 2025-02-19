def get_distance(a, b, N):
    # 일반적인 거리
    direct_dist = abs(a - b)
    # 원형으로 인한 거리
    circular_dist = min(abs(a - b), N - abs(a - b))
    return circular_dist

def check_combination(i, j, k, a, b, c, N):
    # 각 자리별로 거리가 2 이내인지 확인
    return (get_distance(i, a, N) <= 2 and 
            get_distance(j, b, N) <= 2 and 
            get_distance(k, c, N) <= 2)

N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            # 첫 번째 조합과의 거리가 모두 2 이내이거나
            # 두 번째 조합과의 거리가 모두 2 이내인 경우
            if (check_combination(i, j, k, a1, b1, c1, N) or 
                check_combination(i, j, k, a2, b2, c2, N)):
                cnt += 1

print(cnt)