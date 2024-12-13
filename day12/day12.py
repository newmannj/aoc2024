from typing import List

class Node:
    value: str
    x: int
    y: int
    adjacent_count: int
    visited: bool

    def __init__(self, value, x, y, visited = False):
        self.value = value
        self.x = x
        self.y = y
        self.adjacent_count = 0
        self.visited = visited
        self.region = []

    def __str__(self):
        return f"{self.value}"
    
    def __repr__(self):
        return f"{self.value}"

test_garden = [ 
    'AAAA',
    'BBCD',
    'BBCC',
    'EEEC'
]


def as_nodes(garden: List[str]):
    rows = []
    for y, row in enumerate(garden):
        rows.append([Node(plant, x, y) for x, plant in enumerate(row)])
    return rows

def in_bounds(x, y, grid):
    return (
        y >= 0 and
        y < len(grid) and
        x >= 0 and 
        x < len(grid[y])
    )

def find_region(plant: Node, garden: List[List[Node]], region: List[Node]):
    # For all possible neighbors of plant, check if they are the same value
    plant.region.append(plant)
    for i in range(4):
        next_y, next_x = [0, 0]
        if i == 0:
            next_y = plant.y - 1
        elif i == 1:
            next_y = plant.y + 1
        elif i == 2:
            next_x = plant.x - 1
        else:
            next_x = plant.x + 1
        if (in_bounds(next_x, next_y, garden)):
            next_plant = garden[next_y][next_x]
            if(next_plant.value == plant.value and not next_plant.visited):
                next_plant.visited = True
                plant.region.append(next_plant)
    return plant


def count_cost(garden: List[List[Node]]):
    for y in range(len(garden)):
        for x in range(len(garden[y])):
            plant = garden[y][x]
            if not plant.visited:
                plant.visited = True
                print(find_region(plant, garden, [plant]))

count_cost(as_nodes(test_garden))