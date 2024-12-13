from typing import List

class Node:
    value: str
    x: int
    y: int
    visited: bool

    def __init__(self, value, x, y, visited = False):
        self.value = value
        self.x = x
        self.y = y
        visited = visited

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

def find_region_cost(plant, garden, region):
    # For all neighbors of plant, keep adding to region
    for x in range(4):
        if x == 1:
            

def count_cost(garden: List[List[Node]]):
    for y in range(len(garden)):
        for x in range(len(garden[y])):
            plant = garden[y][x]
            if not plant.visited:
                plant.visited = True
                find_region_cost(plant, garden, [plant])