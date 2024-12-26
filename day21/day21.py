keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"],
]

keys = {
    "0": (1, 3),
    "A": (2, 3),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0)
}

r1_p = (2, 3)

directionpad = [
    [None, "^", "A"],
    ["<", "v", ">"]
]

r2_p = (2, 0)
r3_p = (2, 0)
u_p = (2, 0)
pads = [r1_p, r2_p, r3_p, u_p]

codes = []
with open("codes.txt") as file:
    for line in file:
        codes.append(line.strip())

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dirarrows = ["^", ">", "v", "<"]

# Returns the path(s) to the specified character in grid
# from point
def walk(point, grid, character, path, seen):
    # Out of bounds
    if point[1] < 0 or point[1] >= len(grid) or point[0] < 0 or point[0] >= len(grid[point[1]]):
        return False
    # at a bad spot
    if grid[point[1]][point[0]] == None:
        return False
    # At the desired character:
    if grid[point[1]][point[0]] == character:
        path.append(point)
        return path
    # We've already been here
    if seen[point[1]][point[0]]:
        return False
    
    path.append(point)
    seen[point[1]][point[0]] = True
    paths = []
    for i, d in enumerate(dirs):
        next_point = (point[0] + d[0], point[1] + d[1])
        
        result = walk(next_point, grid, character, path, seen)
        if result:
            paths.append(result)
    
    return paths

# Returns the viable paths starting at point
# to print code.
def get_paths(point, grid, code):
    for c in code:
        seen = [[False for _ in r] for r in grid]
        result = walk(point, grid, c, [], seen)
        if result:
            print(result)

for code in codes:
    # Let's just try to solve the first pad
    paths = get_paths(r1_p, keypad, code)
    print(paths)
    exit()


    


