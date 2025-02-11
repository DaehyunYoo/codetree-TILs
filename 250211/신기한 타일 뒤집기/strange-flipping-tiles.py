N = int(input())
line = [0] * 2001  # Array to store tile colors: -1 for white, 1 for black, 0 for gray
position = 1000    # Start from middle to allow left/right movement

for _ in range(N):
    x, direction = input().split()
    x = int(x)
    
    if direction == 'L':
        # Move left and color tiles white
        for i in range(x):
            position -= 1
            line[position] = -1
    else:  # direction == 'R'
        # Move right and color tiles black
        for i in range(x):
            line[position] = 1
            position += 1

# Count white (-1) and black (1) tiles
white_count = line.count(-1)
black_count = line.count(1)

print(white_count, black_count)