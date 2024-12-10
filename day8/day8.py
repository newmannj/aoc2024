from typing import Dict, List, Tuple
grid: List[str] = []
with open("antennas.txt") as file:
    for line in file:
        grid.append(line.strip())

def get_antinodes(antenna_a, antenna_b, grid):
    # Return antinodes of the given antenna locations, removing those that fall outside of the grid
    x_diff = antenna_a[0] - antenna_b[0]
    y_diff = antenna_a[1] - antenna_b[1]
    # Then add x diff and y diff to each antenna
    antenna_a_antinode = (antenna_a[0] + x_diff, antenna_a[1] + y_diff)
    antenna_b_antinode = (antenna_b[0] - x_diff, antenna_b[1] - y_diff)
    
    return [antinode for antinode in [antenna_a_antinode, antenna_b_antinode] if (antinode[1] >= 0 and antinode[1] < len(grid) and antinode[0] >= 0 and antinode[0] < len(grid[antinode[1]]))]

found_antennas: Dict[str, List[Tuple[int, int]]] = {}
antinodes = set()
y = 0
while(y < len(grid)):
    x = 0
    while(x < len(grid[y])):
        antenna = grid[y][x]
        if not antenna == ".":
            # Handle the antenna
            if antenna in found_antennas:
                # TODO:
                #   - Find antinodes of each already found antenna
                for found_antenna in found_antennas[antenna]:
                    antinodes = set(list(antinodes) + get_antinodes([x, y], found_antenna, grid))
                found_antennas[antenna].append([x, y])
            else:
                found_antennas[antenna] = [(x, y)]
        x += 1
    y += 1
print(len(antinodes))