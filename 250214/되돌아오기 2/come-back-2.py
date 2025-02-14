text = input()
order = [text[i] for i in range(len(text))]

# graph = [[0 for _ in range(100000) for _ in range(100000)]]
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
x, y = 0, 0
move_dir = 2

cnt = 0
position = []

for i in range(len(order)):
    if order[i] == 'F':
        nx, ny = x + dxs[move_dir], y + dys[move_dir]
        x, y = nx, ny
        # cnt += 1
    
    elif order[i] == 'L':
        if move_dir == 0:
            move_dir = 1
        elif move_dir == 1:
            move_dir = 2
        elif move_dir == 2:
            move_dir = 3
        else:
            move_dir = 0
        # cnt += 1
    
    else:
        if move_dir == 0:
            move_dir = 3
        elif move_dir == 1:
            move_dir = 0
        elif move_dir == 2:
            move_dir = 1
        else:
            move_dir = 2
        # cnt += 1
    
    position.append((x, y))

ans = -1
for i in range(len(position)):
    if position[i] == (0, 0):
        ans = i + 1

print(ans)