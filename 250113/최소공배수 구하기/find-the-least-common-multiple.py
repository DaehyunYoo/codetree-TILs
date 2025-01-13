n, m = map(int, input().split())

def lcm(x, y):
    # 큰 수부터 시작해서 두 수의 곱까지 확인
    for i in range(max(x, y), (x * y) + 1):
        if i % x == 0 and i % y == 0:
            return i

print(lcm(n, m))