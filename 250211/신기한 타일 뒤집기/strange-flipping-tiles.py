N = int(input())
tiles = set()  # Store colored tile positions
white = set()  # Store white tile positions
black = set()  # Store black tile positions
curr = 0       # Current position

for _ in range(N):
    x, direction = input().split()
    x = int(x)
    
    if direction == 'L':
        # Color x tiles to the left
        for i in range(1, x + 1):
            pos = curr - i
            tiles.add(pos)
            white.add(pos)
            if pos in black:
                black.remove(pos)
    else:  # direction == 'R'
        # Color x tiles to the right
        for i in range(x):
            tiles.add(curr)
            black.add(curr)
            if curr in white:
                white.remove(curr)
            curr += 1

print(len(white), len(black))