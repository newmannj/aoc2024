from enum import Enum
from typing import List

grid: List[List[int]] = []
with open("map.txt") as file:
    for line in file:
        grid.append([int(x) for x in line.strip()])
test_grid = [
    [8,9,0,1,0,1,2,3],
    [7,8,1,2,1,8,7,4],
    [8,7,4,3,0,9,6,5],
    [9,6,5,4,9,8,7,4],
    [4,5,6,7,8,9,0,3],
    [3,2,0,1,9,0,1,2],
    [0,1,3,2,9,8,0,1],
    [1,0,4,5,6,7,3,2]
]

class Direction(Enum):
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"

def move(x, y, direction):
    if(direction == Direction.NORTH):
        y -=1
    elif(direction == Direction.SOUTH):
        y += 1
    elif(direction == Direction.EAST):
        x += 1
    else:
        x -= 1
    return (x, y)

def in_bounds(x, y, grid):
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y])


def get_number_of_high_points(x, y, grid, acc):
    curr_value = grid[y][x]
    high_points = 0
    for direction in Direction:
        next_pos = move(x, y, direction)
        if(in_bounds(next_pos[0], next_pos[1], grid)):
            next_value = grid[next_pos[1]][next_pos[0]]
            if (next_value - curr_value == 1):
                if (next_value == 9):
                    if(f"{next_pos[0]},{next_pos[1]}" not in acc):
                        high_points += 1
                high_points += get_number_of_high_points(next_pos[0], next_pos[1], grid, acc)
    return high_points

def get_score(x, y, grid):
    found_high_point_coords = {}
    return get_number_of_high_points(x, y, grid, found_high_point_coords)

def calculate_map_score(grid):
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if(grid[y][x] == 0):
                total += get_score(x, y, grid)
            x += 1
        y += 1
    return total

print(calculate_map_score(test_grid))
print(calculate_map_score(grid))