import enum
# Part 1: All XMAS occurrences
search = []
with open("words.txt") as file:
    for line in file:
        search.append(line.strip())

# Idea: Treat it as a graph, find the first X, then iterate over all edges until XMAS is found
# Or not found

class Direction(enum.Enum):
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    WEST = "WEST"
    EAST = "EAST"
    NORTHWEST = "NORTHWEST"
    NORTHEAST = "NORTHEAST"
    SOUTHWEST = "SOUTHWEST"
    SOUTHEAST = "SOUTHEAST"

"""
XMASX
MMSAM
AXAAA
SASSS
"""
def find_xmas(x, y, search, acc, direction):
    if (direction == Direction.NORTH):
        y = y - 1
    elif (direction == Direction.SOUTH):
        y = y + 1
    elif (direction == Direction.WEST):
        x = x - 1
    elif (direction == Direction.EAST):
        x = x + 1
    elif (direction == Direction.NORTHEAST):
        x = x + 1
        y = y - 1
    elif (direction == Direction.NORTHWEST):
        x = x - 1
        y = y - 1
    elif (direction == Direction.SOUTHEAST):
        x = x + 1
        y = y + 1
    elif (direction == Direction.SOUTHWEST):
        x = x - 1
        y = y + 1
    # Bounds Check
    if y < 0 or y >= len(search) or x < 0 or x >= len(search[y]):
        return False
    
    result = acc + search[y][x]
    
    if result == "XMAS":
        return True
    if result in "XMAS":
        return find_xmas(x, y, search, result, direction)
    
    return False

def find_xmas_count(x, y, search):
    current_xmases = 0
    for direction in Direction:
        current_xmases += int(find_xmas(x, y, search, "X", direction))
    return current_xmases

total = 0
y = 0
while(y < len(search)):
    x = 0
    while(x < len(search[y])):
        if search[y][x] == "X":
            total += find_xmas_count(x, y, search)
        x += 1
    y += 1
print(total)


def is_crossmas(x, y, search):
    # Bounds. We shouldn't have a low-bounds issue 
    # since we're starting at 1.
    if y + 1 >= len(search) or x + 1 >= len(search[y]):
        return False
    # Check nw
    northwest = search[y-1][x-1]
    northeast = search[y-1][x+1]
    southwest = search[y+1][x-1]
    southeast = search[y+1][x+1]
    # Both North s, both south M
    if (northwest == "S" and northeast == "S" and southwest == "M" and southeast == "M"):
        return True
    # both west M, both east S
    elif (northwest == "M" and northeast == "S" and southwest == "M" and southeast == "S"):
        return True
    # both south S, both north M
    elif (northwest == "M" and northeast == "M" and southwest == "S" and southeast == "S"):
        return True
    # both west S, both east M
    elif (northwest == "S" and northeast == "M" and southwest == "S" and southeast == "M"):
        return True
    return False
    

# Part 2: Find cross-MAS
total = 0
# We can start in the second row/column, because the shape is going to be 3x3
y = 1
while(y < len(search)):
    x = 1
    while(x < len(search[y])):
        if search[y][x] == "A":
            total += is_crossmas(x, y, search)
        x += 1
    y += 1
print(total)