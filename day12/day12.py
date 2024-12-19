grid = []
with open("test_input.txt") as file:
    for line in file:
        grid.append(list(line.strip()))

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

seen = [[False for c in row] for row in grid]

curr_region = []
regions = []
for y, r in enumerate(grid):
    for x, c in enumerate(grid[y]):
        if not seen[y][x]:

