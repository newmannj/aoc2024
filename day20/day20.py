grid = []
start = None
with open("input.txt") as file:
    for y, line in enumerate(file):
        grid.append(list(line.strip()))
        if "S" in line:
            start = (line.find("S"), y)

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
import sys

sys.setrecursionlimit(100000)  # Set the new limit to 2000
print(sys.getrecursionlimit())

def walk(curr, grid, seen, path):
    # Base case: we're off the grid
    if curr[1] < 0 or curr[1] >= len(grid) or curr[0] < 0 or curr[0] >= len(grid[1]):
        return False

    # Base case: we're at the end
    if grid[curr[1]][curr[0]] == "E":
        path.append(curr)
        return True
    
    # Base case: we're on a wall
    if grid[curr[1]][curr[0]] == "#":
        return False
    
    # Base case: we've seen this node
    if seen[curr[1]][curr[0]]:
        return False
    
    # pre
    path.append(curr)
    seen[curr[1]][curr[0]] = True
    # recurse
    for d in dirs:
        if walk((curr[0] + d[0], curr[1] + d[1]), grid, seen, path):
            return True
    # post
    path.pop(curr)
    return False
    


def solve_track(grid):
    seen = [[False for _ in r] for r in grid]
    path = []
    walk(start, grid, seen, path)
    return path

# first, get the path with no cheats
base_path = solve_track(grid)

# base_path = base_path[1:]
# then, can we iterate on this path and try to solve
attempted = [[False for _ in r] for r in grid]
test = {}
p1 = 0
for p in base_path:
    for d in dirs:
        cheat = (p[0] + d[0], p[1] + d[1])
        if cheat[1] < 0 or cheat[1] >= len(grid) or cheat[0] < 0 or cheat[0] >= len(grid[1]):
            continue
        if attempted[cheat[1]][cheat[0]]:
            continue
        if grid[cheat[1]][cheat[0]] == "#":
            # If we are at a wall, then we should try a cheat
            # We shouldn't need to resolve, we can just go two times in that direction
            # If we're later in the path then we can say that that cheat will save time
            attempted[cheat[1]][cheat[0]] == True
            after_cheat = (cheat[0] + d[0], cheat[1] + d[1])
            try:
                after_cheat_index = base_path.index(after_cheat)
                if after_cheat_index:
                    seconds_saved = after_cheat_index - (base_path.index(p) + 2)
                    if (seconds_saved > 0):
                        # print(seconds_saved)
                        if seconds_saved in test:
                            test[seconds_saved] += 1
                        else:
                            test[seconds_saved] = 1
                    if (seconds_saved >= 100):
                        p1 += 1
            except ValueError:
                continue
print(p1)
# print(test)

# Part 2: For each node in the path, do a number of DFS
# Ooh, maybe we can eliminate some of the search area since 
# we are only interested in responses that save 100
# microseconds or more.
