def check_distance(comb1, comb2):
    # 각 자리수별로 거리 확인
    for i in range(3):
        if abs(comb1[i] - comb2[i]) <= 2:
            return True
    return False

N = int(input())
a, b, c = map(int, input().split())
given_combination = (a, b, c)

count = 0
# 모든 가능한 3자리 조합 확인
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            current_combination = (i, j, k)
            if check_distance(current_combination, given_combination):
                count += 1

print(count)