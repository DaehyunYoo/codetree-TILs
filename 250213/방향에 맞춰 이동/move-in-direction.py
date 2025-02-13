N = int(input())

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
x, y = 0, 0

for _ in range(N):
    d, w = input().split()
    if d == 'E':
        nx = x + int(w) * dx[0]
        ny = y + int(w) * dy[0]
    elif d == 'N':
        nx = x + int(w) * dx[1]
        ny = y + int(w) * dy[1]
    elif d == 'W':
        nx = x + int(w) * dx[2]
        ny = y + int(w) * dy[2]
    else:
        nx = x + int(w) * dx[3]
        ny = y + int(w) * dy[3]

    x, y = nx, ny

print(x, y)
