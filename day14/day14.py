import math
from typing import List, TypedDict
import time

class Pos(TypedDict):
    x: int
    y: int

class Velocity(TypedDict):
    x_diff: int
    y_diff: int

class Robot(TypedDict):
    cur_pos: Pos
    velocity: Velocity

robots: List[Robot] = []

grid_width = 101
grid_height = 103
grid = [[[] for _ in range(grid_width)] for _ in range(grid_height)]
with open("robots.txt") as file:
    for line in file:
        new_robot: Robot = {}
        split = line.split()
        position = split[0].replace("p=","")
        positions = position.split(",")
        new_pos = {"x": int(positions[0]), "y": int(positions[1])}
        new_robot["cur_pos"] = new_pos
        grid[new_pos["y"]][new_pos["x"]].append(new_robot)

        velocity = split[1].replace("v=", "")
        velocities = velocity.split(",")
        new_velocity = {"x_diff": int(velocities[0]), "y_diff": int(velocities[1])}
        new_robot["velocity"] = new_velocity
        robots.append(new_robot)

def print_grid(grid):
    for r in range(grid_height):
        print("".join([str(len(grid[r][c])) if len(grid[r][c]) != 0 else "." for c in range(grid_width)]))

def move_robots(robots: List[Robot], new_grid: List[List[List[Robot]]]):
    for robot in robots:
        
        next_pos_x = robot["cur_pos"]["x"] + robot["velocity"]["x_diff"]
        if (next_pos_x < 0):
            next_pos_x = grid_width + next_pos_x
        elif (next_pos_x >= grid_width):
            next_pos_x = next_pos_x % grid_width
        next_pos_y = robot["cur_pos"]["y"] + robot["velocity"]["y_diff"]
        if (next_pos_y < 0):
            next_pos_y = grid_height + next_pos_y
        elif(next_pos_y >= grid_height):
            next_pos_y = next_pos_y % grid_height
        robot["cur_pos"] = {"x": next_pos_x, "y": next_pos_y}
        new_grid[next_pos_y][next_pos_x].append(robot)

def get_safety_code(robots):
    # Step 2: Figure out the safety factor
    quadrants: List[List[Robot]] = [[], [], [], []]
    for robot in robots:
        if robot["cur_pos"]["x"] < math.floor(grid_width / 2):
            if robot["cur_pos"]["y"] < math.floor(grid_height / 2 ):
                quadrants[0].append(robot)
            elif robot["cur_pos"]["y"] > math.floor(grid_height / 2):
                quadrants[2].append(robot)
        elif robot["cur_pos"]["x"] > math.floor(grid_width / 2):
            if robot["cur_pos"]["y"] < math.floor(grid_height / 2 ):
                quadrants[1].append(robot)
            elif robot["cur_pos"]["y"] > math.floor(grid_height / 2):
                quadrants[3].append(robot)

    return len(quadrants[0]) * len(quadrants[1]) * len(quadrants[2]) * len(quadrants[3])

# Step 1: Do the move
minimal_safety_code_i = 0
min_safety_code = None
for i in range(1000000):
    new_grid = [[[] for _ in range(grid_width)] for _ in range(grid_height)]
    move_robots(robots, new_grid)
    safety_code = get_safety_code(robots)
    if min_safety_code is None:
        min_safety_code = safety_code
        minimal_safety_code_i = i
    elif min_safety_code > safety_code:
        min_safety_code = safety_code
        minimal_safety_code_i = i
        print(i)
        print_grid(new_grid)

print(minimal_safety_code_i)
