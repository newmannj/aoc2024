from enum import Enum
from typing import List

class Posn:
    x: int = None
    y: int = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"

class Direction(Enum):
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"


map: List[str] = []
start_posn = Posn(0, 0)
with open("positions.txt") as file:
    for i, line in enumerate(file):
        map.append(line.strip())
        if "^" in line:
            start_posn.y = i
            start_posn.x = line.index("^")

# Loop condition: until the position is off of the map
def is_out_of_bounds(posn: Posn, map):
    return posn.y < 0 or posn.y >= len(map) or posn.x < 0 or posn.x >= len(map)

# Part 1
def get_unique_positions(start_posn, map):
    visited = {f"{start_posn.x},{start_posn.y}": True}
    direction = Direction.NORTH
    while(not is_out_of_bounds(start_posn, map)):
        move_posn = Posn(start_posn.x, start_posn.y)
        if (direction == Direction.NORTH):
            move_posn.y -= 1
        elif (direction == Direction.SOUTH):
            move_posn.y += 1
        elif (direction == Direction.EAST):
            move_posn.x += 1
        elif (direction == Direction.WEST):
            move_posn.x -= 1
        # TODO: Do we really need two condition checks
        if (is_out_of_bounds(move_posn, map)):
            break
        if map[move_posn.y][move_posn.x] in [".", "X"]:
            start_posn.x = move_posn.x
            start_posn.y = move_posn.y
            new_key = f"{start_posn.x},{start_posn.y}"
            if (not new_key in visited):
                visited[new_key] = True
                s = list(map[move_posn.y])
                s[move_posn.x] = "X"
                map[move_posn.y] = "".join(s)
        elif map[move_posn.y][move_posn.x] == "#":
            if (direction == Direction.NORTH):
                direction = Direction.EAST
            elif (direction == Direction.SOUTH):
                direction = Direction.WEST
            elif (direction == Direction.EAST):
                direction = Direction.SOUTH
            elif (direction == Direction.WEST):
                direction = Direction.NORTH

    print(len(visited.keys()))

# get_unique_positions(start_posn, map)


# Part 2:
# Idea:
#   If you get to a position that has been visited, try taking a right and travel all the way down
#   If there is an obstruction before you get to the edge, then you can place an obstruction there

visited = {f"{start_posn.x},{start_posn.y}": True}
direction = Direction.NORTH
while(not is_out_of_bounds(start_posn, map)):
    move_posn = Posn(start_posn.x, start_posn.y)
    if (direction == Direction.NORTH):
        move_posn.y -= 1
    elif (direction == Direction.SOUTH):
        move_posn.y += 1
    elif (direction == Direction.EAST):
        move_posn.x += 1
    elif (direction == Direction.WEST):
        move_posn.x -= 1
    # TODO: Do we really need two condition checks
    if (is_out_of_bounds(move_posn, map)):
        break
    if map[move_posn.y][move_posn.x] in [".", "X"]:
        start_posn.x = move_posn.x
        start_posn.y = move_posn.y
        new_key = f"{start_posn.x},{start_posn.y}"
        if (not new_key in visited):
            visited[new_key] = True
            s = list(map[move_posn.y])
            s[move_posn.x] = "X"
            map[move_posn.y] = "".join(s)

    elif map[move_posn.y][move_posn.x] == "#":
        if (direction == Direction.NORTH):
            direction = Direction.EAST
        elif (direction == Direction.SOUTH):
            direction = Direction.WEST
        elif (direction == Direction.EAST):
            direction = Direction.SOUTH
        elif (direction == Direction.WEST):
            direction = Direction.NORTH

print(len(visited.keys()))
