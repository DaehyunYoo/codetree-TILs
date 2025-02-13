N, T = map(int, input().split())
R, C, D = input().split()
x, y = int(R), int(C)

mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}
x, y, move_dir = x - 1, y - 1, mapper[D]

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N


for _ in range(T):
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    if in_range(nx, ny):
        x, y = nx, ny
    else:
        move_dir = 3 - move_dir

print(x+1, y+1)