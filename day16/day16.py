from typing import List

test_maze = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""

grid = [list(row) for row in test_maze.splitlines()]

# Find Start
start = None
# We start facing East
current_direction = ">"
for y, r in enumerate(grid):
    for x, c in enumerate(r):
        if c == "S":
            start = (x, y)
            break

directions = [">", "v", "<", "^"]
print("Start: ", start)

def get_next_location(location, curr_direction):
    x_modifier = 0
    y_modifier = 0
    # Then, we check the next location
    if curr_direction == ">":
        x_modifier = 1
    elif curr_direction == "v":
        y_modifier = 1
    elif curr_direction == "<":
        x_modifier = -1
    elif curr_direction == "^":
        y_modifier = -1
    next_location = (location[0] + x_modifier, location[1] + y_modifier)
    return next_location

def get_path_score(path):
    total = 0
    for m in path:
        if m == "s":
            total += 1
        elif m == "r":
            total += 1000
    return total

def find_cheapest_path(location, curr_direction, grid, moves: List[str], visited: List):
    visited.append(location)
    paths = []
    for direction in directions:
        new_moves = "r" if direction != curr_direction else ""
        next_location = get_next_location(location, direction)
        next_value = grid[next_location[1]][next_location[0]]
        if next_value == "#" or next_location in visited:
            paths.append([])
        elif next_value == ".":
            new_moves += "s"
            paths.append(find_cheapest_path(next_location, direction, grid, moves + list(new_moves), visited))
        elif next_value == "E":
            new_moves += "s"
            paths.append(moves + list(new_moves))

    actual_paths = [path for path in paths if len(path) > 0]
    min_path = []
    min_score = None
    for path in actual_paths:
        path_score = get_path_score(path)
        if min_score is None or path_score < min_score:
            min_score = path_score
            min_path = path
    return min_path

cheapest_path = find_cheapest_path(start, ">", grid, [], [])
print(get_path_score(cheapest_path))