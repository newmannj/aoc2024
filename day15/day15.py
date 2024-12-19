warehouse_2 = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########
"""

moves_2 = """
<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""

warehouse_1 = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########
"""

moves_1 = """<^^>>>vv<v>>v<<
"""

warehouse_actual = """##################################################
#...O....OO.#O......#...#........#..O..OO.......O#
#.OO#....#.#O..#O.......OO..O.O.O.O.OO..##..OO...#
#O....#O.........O.O.OOO.O..#..OO.O...O..........#
#........O...OO..O..OOO..O.O##...O.O...O..OO.O...#
#...#.#...#.#.O..O.....#...O..OO.O..O....O#..O...#
#.O#.O....O..O.#.....O..O........O.O........O..OO#
#..OO#O..O..##.......O...#...O....O.....O.O...#.O#
#....O...O......O#.O......O......O...O.....OO...##
#.O#.#O.O..O.#.OO........O......#.O.....O..O.#...#
#.O.OOO.......OOO.O.OOO.O.#....O..#....O....O..O.#
#OO.O.....#.#......OO.OO.O.O.#..#..O..#.....##..O#
#...#.O.....OO..O...O...OO.....#..O...#...O....O.#
#.O.O.O............OO.OO#..OO.#.O..#..OOO....O...#
#......#.O.O..#.#O....OO.......OO.O...OO.OO......#
#..O......#O...O.O.#..O.O........O......O...#....#
##O.O#.O#...O...OO..O......................O.....#
#OO....#..OO#O..O..OO.O......O.O..#...O..O...O..##
#.OOO..O...OO...O..OO#..OO#........O.##..O..#O.O.#
#..O..O.OO#...O...#O....O..O.......O..#.#.OO.OO..#
#O.O.O.OOO..#...#..O#O.O...#O#...O.O.O#O.OO.O..O.#
#O#.#........OO...#..#O#.O..#O.OO....OO..O#.OO.O.#
#O..OO..OOOO......O#..O.O#.......O.#O....O.....O.#
#OO..O#..O#....#O.....O....OO..O.O.O.#...#.##....#
#.....O.OO...O..O.......@....O...O..OO....O..#..##
#..O..#..................#............O.#..O.#O..#
#...O...O.OO.O..#..OO..O....O.O..OO.OO#..O....#.##
#.OO.O#.O...O..##..#..O...O.....OO#..#.O.O...OO..#
#OOO.OO..#OO...OOOO...OO...........#...#.O#..##..#
#.O...........OOO....O..O..#...O......O.O......OO#
#O.O..O.OOO#O.......#..O.O.O.OO...O...O..O#O.OO.##
#..OO.....O.O...#....O....OO.....#......#.O#OO##.#
#.O.OOO.O.O.#....O.#O.O.........O.#....OO...O..###
#O...O#O.....#.#O....O.....#...#O..O.OO..O....O..#
#.OO.O..#....#..O......O..#..........OO..O.O..OOO#
#O....O..O........O.#.O..........O...O...OOO#...O#
##O..#.....OO..OO...OO.......O..OO.OO.....#.#..O.#
#O..OO#O...#O..O....#.#.O.O............O..#......#
#....O.#.O.O...O...O.OO......#..O...#.........O#.#
#OO..O...OO.OOOO...OOO.O..OO.......O.O.OO..O.O.O.#
#......O....O##....OO.O.....#.#....OO#.OO........#
#...#.O.#.#....O.........#O.O....O#.O...O..#.O..O#
#O.#.O....O.........O.OO.#......O#..O#O.O....O.OO#
#..OO#.......O..........O..#.O..........O..#.OO..#
#..........#..OO.O#.........O...O....O#......#O..#
#.O.#.#.O.OO.O.O.OO...O..#O.O.O...O.........O###.#
#.OO.#.....#O.....O.OO......O..........OO#...O...#
##....O#.....O.....O....O.....O.O..O........O..#O#
#O.O..O#...O..OO..O.OO.O..O...O.......O..O.O.O...#
##################################################
"""

moves_actual = """>>>>>>>>>^<^><v<>><>^^<v^v^<>v<>^v<^<^<^v<<><<<>><<v<<>><<<<<v><v<^v^v^v<<v^<^<^<>>^^vv^<<><<>^<v>^<^v^>v>><^>>vvv<<>^^<^^^>><v^v>^><<v<vv<>v^v<^<^^<>>^vv^>^>><>>>vv>^^^>v^v<<><vv<<^^>^<<vvv^vv<>v>>>>v<>v<<^>v>v<v<>>^v<><vv<vvv^><<<><v><<v^>^^v><>v>v>^<^^<^v>>^vv^^^<>^<^v^v<^v^<vv<>><>>>v>^><^<vvvv^>v>v^>^>^>>v^vv<v><v>^^<><v>^>vv>>^<^<^v^><<>^vvv<^v<^v^<<v>^^>>^><vvv><>v<v^>^v^<^<v^^v<vv>v^<<<^^^v>v^^>vv>v<^>v<^v>v>v>^<^v<^v^^>><>>><vvv>vv^^>v>^^>vv<^v<>v^v>^<^>vvv^>v<^>><>vv<>>^<^<v<>v<^^v^>v><<<v><^^>v^>>v^<<<^^^vv^<<v>^>>^>>^^^><<vvvv>^v^^^^^vv<^<^><v>v^>^^<v^v<^^v^<v>vv>^><^<<>>^>^^>><v^<<<<>><<vvvv^^<>>^>>v>><>>v^>^<>v<vv>>>^<><>^^v>^<<v<<><v<^<<><vvv^^^<vv>v<<<vv<v^^v^>^<>><><v^v><^v^vv>^v^v<^v^<^^>>v^^^>>v<<><^^v>v^<^^<<^<v>^<<<^v^>^^>vvv^>v^<vvv<>^^<<>^vv<<^>v^<><<<<v>>v^<^^v><^v^<><^v<vv<^>^v>^<<<^v^<^^<^<v><<<<^<^>>>^<v>v^^<vv<^vv<v>^v^v^^v^^<v><><vv<>^^^^><>^<^><^v^v<<^>^<^><><^v^<^^vvv>>^>^^^^v^>^^<^v<<v<vv><<>><^v^^^v^^v<<^^v<><<>v>>^<>v>^<<vvv<v<^<>v^<<>><>^<^>v^^>v><^><
^>>^>v>^>v>^^><>>^><^^^>v<^<>><^>v<<v^<v<>vv<^^^v^>^>v><<><<^>v<>v^^v<vv^>>v^>v^>>^^>v>^<^v>v<^<<^<^v<>v<>><><^vv<v<^^><>><vv^>^v^^v>>>>>v^vv<v><^^v^v<<^<^^^^<<vvv>>^^<<v>^>^^^<^v<v^^<v^>v<>v^><v<<<^^>v<vv>vv^>v>v^v^<<v><<^^v>^><v<>>vv>v^<^>^<v<v^^^<>v<^><<<^^vv><>><^v>><<^^v<v<><^v<>v^v^<v>^><<>^v<<<vv^><v^<^<<><^^<><v<^^<<v<>>^v^<v^<>>><^<v<<v<^>v<v>>v^v<>><>^vvv><v^<^<v^vvv<^<<<>>^<v^^v^>v<<>^>>><<^<>>>^<>v<v><v<<>v^v<^v^^^v^^v><^^v>^^>^>v^^v<<>v<<v>v^><v^>v<vv>><>^>>^^^<>vvv<v>v^^v^<^v^>>>v>^^<vv>^^>><^^>><><^>v<^>vv>^vv^>^^^vv>vvv<v<^<v<<>vv<^<>^><v<>^>vv^<>^<><>^>><^>^^v<v><v^<v>v>^<>^<^<^>><^<>>^^v^^>v^<^^^vv<<^<v<<v<><<^^>>>>>><vvv^^>>>v^><^^vv^<<<^<v^^^v^^v<<v^<>^<^>><^>^vv>>^>^<<^^<v>><v<^>^^v^>><v<^<<^<^v>v>v^>^>v>>^><^<>>>v>v><<<>^<v<>v>><<^^v<<v<>^<>v^v^v>^^v<<>><^vv>>>v^^>^v>v<^^^>>>^<^<^<^v>vv<^^<>>^vv<vv^<vvvv>v^^^<>v<>><<^^^^v<^vv^><^<<^<<^v^^<<^^>>>^>>v^^^v>^^^^><^>>>vv^^v<<v<^<v^>>>^v^<>>^>><^<><^<<v>^>v>v^^<v<v^>><^>v<<>^<>v>>>^^vvv<vvv^^<>v^v>^<<vv><>^v>^v^v<<v^>vv
v^>>>^^<<^<^<<v^>v>v>^<<<<><>v^^^>^>v>vv^^v<^>^<^^^<>v^>vvv^<^^^vv<>^<^>^^v>^^>v>v^vv^<^^<v<^>><>v>>^^v^^>>v>v><<vv>^v><^>><<><v><>^vv<>v>vv><>>><<v<^v<>v><>v^v<^^<<<>v><<vvv^>^><>^v>><>><v^><^>v>^>^<<>^vv^<v<^<v<^<v^>vvv^><vvv>^<<<<><^>v<><<<^<v^<^<^>^<^^<>v>><><<<v^<>^>vvv^>^>^<>^^^<^>^<vv<v>v><<v<<>v<v<vv>v<<>>vv^>v>vv><<^v^>^<>v>>^<v>vvv>^v^v^v^<<>>^^^^^<><>^><>v><^^<v^<^>v<^^v>v<v<v^^>>>>^<vv<v<vv><<^^>><v>>v^<>v^>v^<<^>v^<^<^<vvv<^v>>v^^^v^v<^v>>^^v>^<v<<>v^>>^v^v<vv><^^><^v>^>^^v<>^^^>^>v>^><v<><^v>>>v^><^<<<^v<<v>^^<^<vv<<>>>>v><>v^v^v><>>>^>vv<<v<><<^>>>>>^v>vvv<>>vv><^v<vv<<vv^>^<^^^^^><v^^>v^^<^<>^>vvvv^^>>^^v>vv^v<^vvv><<<^<<^v><>><>^^<<><^><v^>v^v>>v><>^<v^^<<v><^^v>^><v>^>v<>v<>><^>^^>^><<vv^v<v^>><^^^vv<^^^<>><><<><^vv^>^>^^>>vv^><>vv>v>v>v>v>>>^^vv^><^^^vv^<vv>^vv<>^>v>v<v<^><>v<v<v^^v^>v<^>^vvvv^<v<<<v<^v<<<<^^v><<<><v^>v^^v<vv^v<^>><^<<v<<v<^<^^>^>><<v>>>^^<<vv<^>vv^<^v>v>^v<^<<vv>^>v<v^>v^>^<^<v<v>^^^><<<vv^v<^v^^>v^vv^<<>v<v^v<<<<<v<^>>><vv<^v><^>v<<^^v^^><vv^>^<^>v
^v>v<^^<>v<><<<^><>>^^<v<>vv^>v>^<>^^^<v>^<<>^v>^<^<<v><<^>v<><v>>^>><^<>^v>vv>^^^<>v><^^^v>v^^>v>^^>^>>v^v>v^<v^<v<<vv>^^<v<^>v>^>^^<^v<^<<^>vv>vv>v>vv^><<<>v>^>vv<^><v^vv<<<<v>>v^<><^>^v^v<<^^>v>^v^^><v^v><^<><^<<><vvv^v^^<<<^<v><v^>>v^>^<v>^^>^<<^<<<><<>vvv^v<^vvv^>^<>^<<>vv<>><>v<^>v<v^^<^v^<v<<>v>>v^>vv<>v^^>vvv>>>^>><^^v^^>^>><>>^v>><><^>^>^v>^<^<>>vv<>v<><>>>^v^<<vv<v^^><<<<v^vv^vv>^<v^v^vvv<^v>><vvv<>v<^v^v^<^>^v^vvv^v<v>vv^<v^>>>v^v^v^^><v>><<>><>v><>>^v<v><vvv<v>^<^<<v^>v<<^<v><<v<^^^<v<^<v>v><><<><v^v<v<<v^><v>v>v>v<^^<>>vv<^^>vv^v>>>v><v^>v>^vv>>vvv^<><v>v<<v^><v><v<v^>>v^><>>vvv><<v>v><^><v^><<vv>^^v<>^<v><v<<<<^^<^vv><<^>>><v<<vv^^<<^v<v^>>^<^<v<v^^>^^<<^v^>v>><<<>^vv<v<>>>v<v>v>>^<^>^^^<<^>^>>>><>^>>^<>^>v><v^<<<v>>^>^v><>v^v^v^><^^v><<><>^<v<><^vv><^<<vv^v<><^<^>v>v<vv>v<>^>^^^^vv^v^<^<^v^>v><<<<vv<><^^^vvv<<^^<<^>v><>v^<^>>>^v^>v<>>^v><^^>^^>>v<^vv^<^<^^v^<^>^>v>v^<>><<<<v^>><^<^<^<vv>^>><>>v<><v<^<<^^<><^<v<<v^<>v^^<<<v<v>v>><>>vv><<^v<^v<^v<v^vv><>^<^>v^v<>^<<v^^>^><
><<<>^<^v>^<v<^<^v<><vv>^^v<vvv<^<>^vv^v>^>><v><>v<^<<^v<>^vv<>v>><<>>>v^>v^^<><>^>v<>v^>vv<v<>>>>^<><<v^>^<>v^>><>v<v<<^^^<^vv^<^^<<^^^v>>v>vv>^^<vv^<>>v<^^>v<<^<>>>>^^^^>>vv>^>v^><v<vv>>>>v^v^><^vv<^^^v<vvvv^v<^><<<<<<v>>>v>^v><<v^v>v^vv<<<^>^^v^^>^^^^>vv><<^<^^^<v><^<v><><v>><^>v<v>^>v^v<v><^<>v><^^<^^><v<>><v<vv^^vv>^^v^><<v><^^v^<v>^<vv^<<><>^>>>>>vv^<<<v>^vvv<<^^<v^<^<vv>^v>>><>>v^^>>v>>vv><<>>v><v^>^><^>v><^>^^^^>vv>^<^<v<v<<^^v<>^<><vvvv>>v^v<vv<v<><<^^v>^^^<>vvv<<>^<^v<v><<<^>v><<<^>>>v<v<vv>>^v^v<<<>>><^>vvv<vv<vv^<>^v^>^>^^^>>^^^<<vv>>>><<v>v>^^v<^^>v><<>><^^^><<v^>v^<^>^>^<>><<<><v>>>v<<><<v<v^><v<>>^v<v<v>^vv^^^^^v>><>^<^^v>^><<>>vv^^><vv^>><<><>v<<^^>>^<v<><>^^><>^<^<>vv^vv>^^^^<<><<vvvv<<^>>v^v<>>vvv<v^<^^>>^>^>><<v>><v<^vvv<^>>^v^^v>^>v^vv<v^v>^^vv^>^>>>^>vvv^>v^^>^v<>><<^^<>vv>^><>^v^>^><<><>^^<vvv^<^vv^^v<v>>>^^<<^<v<<<^>^^v>v^>>>^^v<v><<<v<<^v^^^^v^><^<><<>v<^>v>^<>v>^<<<v^v^^^>>>>vv<<<>><>>v>^>>>v^<<^>v>vvv^v>vv<<^><>^<<<v<^v^^>>^^>v>v^v^v><vv><^>><>^vv><v><^v<v>v<>
>>vvv<<<>>>>^<v<vv<<>^<v>^v>v>^^<>>>^^vvv>^<<<v><<>>^^<>^>><<>^^<^>v<<>v<>v<>^<><^vv^<>^<><vv>^v><vv^<^<<^^<^^<^^<v^<<><vv>v>><<<<>^v^><^>v>v^>^>v>^<<^<>^^><<><>v^>^<<><v>>>v^>v><<>v^vv>vv^><<^>^v^>vv^v<>^^>vv><><^<v^>vvv^<>v<^v<>^<^<>v^vv>vv>>>vv<^<v<>>^v<^<^<>><<>v<><v^^v<v^><v<^>^>^^^>^>><><^^vvvv>>vv<v^<>^<>v>>><v>>^<<><<v><<v^^>><>^vv^^>^^>>><^v^><<>^^v>^>^<<><<>>>>>vv<^>^^<^^vv<^^v>>^^v><vv<>v<^<<<<<>^><^vv^>><<^>vvv>^v^^<^v<><><><vvvv>>>v^<vv<<><^vv>vv<v<^vv<<vv<<vv><>>vv>^<<^^vv^><^^vvvv>v<>v^<^v<^^><>>^vv<vv<<v><<<v>>>><<^<<>v^<v<v^vv>^<>v<v>vvv^^<><v<>>^v<>><<^v^>>^^^v^^<^v<vv>^>^><>v<^^v>^<<v<<>vvv^v>^^^<<>v^^v<><>^^vv>v>v<vv>^^v^^>><v^<^>v^<>^<<<<v<<^^>vv>^v><^v<vv<<<^<^v>>><^<v>>^v<^<>^v<^v<^v^>v>v^><v>^<<v<vv<<^^^><>>v^<>><^vvv>>v^<^><^><<v<v><>^^<>v<v><v^>v<v^>^>^^v<>v^<v^>v<^<><^v<>^^>>^<>vvv<^>^v<^>v>^>v>><<<>>v>^>^^^>>^v^v<<>^v>v>v><<<<<v^^v^<v>^>^v><<>>>^>>v>>^^><^<<<v<<<<vvv^>^><v>^^<^>>^^>vv^v><v^><v>v^<^><<>^v^><v^vv<^^v>v<^>^<><^v<^^>^^>^>^>>v^v>^><^>^vv^><<^>v<v
>^v>^^^^>>vv>v<v><<v<<<<<<>^v^><^<<^v<<^v>><v^^v<v<v<<><<<^<v<<vvv^<^><^<^><^v<v>>><<v>^>vv<v>^>>v<^vvv><vvvv>^><>>>>^<^<><v<>^<^^v>>>^<<vv^<<><vv<<<^^v<^>vv^v<>v<<v><v<v<v^^^v>><^<^>>><><<v<^^<><v^v^><v^v<<<v^^v^<<><^<<>>^<^<<>v>vv^><^^<<vv^>^v<<>^^^<^v<vv><<^<v^>^vvvvv<^<vvv<^vv^<<^^v<v<v>v<^>^<^>>>><>>>^v^<><v>v>^^^^v^^vv><<<^<<<>v^v<<<vvv^vv><<^^^>><v^^^^<^v>><^<v<v>^>>^><^v^v^vv<v>^^v^<>v>><<>^v<^vv^<<vvv<v>^^v>^^>^>v>^v^>v^>v^v<^^>v<v^<><<^^<vv<^v>>^^><<vv^v<vv>v^<<>><>^^v>>v<^>^^<<^^v^>>>^v<v>v^^^^v<>>^v><>v^^>v>v><v^><<^<v>>^^>>v^<>>>^<v^v^<<^^vvvv>^^vv>^^^><^v>^v>^^v<v<<^vv>><v<^^>^<v>>>^<^<<>>v<^>>><<<v^^>>^^vvvv><>vv<><v<v>v<>^<v>><^<><v^^>^^<<v^<<^<vv^^><<^^^v<>^^vv^v<<^^<<^v^<v^<^><^<<><^^>>>vv^>^v>v^^^<^^^^>v<^v^<^>v<v>v^><vv>v<><<<^>>>^^<<<v<v><^v><vv><v<vv><>>^vv<<>^^>v>^^<v^>>^>>v^^^^^^<^^<<^<^<^<^vvv<<v^>>v^<<<>v^v^><v>><<vvvv<><><^>^v<^v>>^><vvv>><>v^^>^v<<>>v<<<>v<vv<>^v<v^<<^^^^^>^<vv>v<vv>v>>^vv>v<><v>v^<>>v<>>v>v^^^v>>>>>v^>vv^^^v^^>>^>^v<^^>v<^><>^<^vv>>^^^<<v<>
vvv^<>^v<<^^^v><^vv>vvv<v>>>^^<v<<>><><v<>v<><^<>^^^^<^>^^^^<v^^>v<^<>vv^v>v>v><><^^>>>>>^<<v<>^^^<>v^^>vv><<<>>vv<v>^>vv<<>v>v><^v<v<<vvv<<^^^vvv^^<^vvv<<><<^<v>>vv<>vvvv>vvv<^v<>>^<^^v^>^vv^^<v^<>vv>>v<>v>^v^vv^>^v^<vv>^^<<^v^^>><>v<vvv<vvv^^vvv^>^^v<<^>v^<v>v<>^^>>^<>>v<<>v<<>>^v^><>v^^^^^><><<<><v>^^vv>v^>^v><><^v^^vvv^>>v^<v^^vvv^<v^^^^^<>^v^v<^vv^^<>v>v<v<v><>>^>vv^><vv><v^v^<><^<^>>vv<^vv>^v>^<v^<v^^^<^<^>^v>v^<<vvv<v^v<vv><v<v><>^^v^v<^>v<<>^^<^>><<<^<vv^v><v<vv>^v>>>>><<v^v>v<vvv>v<v<>><<v<^v^v>>^>>>v><><^v^<v<>>vv^<<v^v>v^><v^>^>><^<<^>>>>v>><<<>v>v^v^>>v^v^v<<^^^<<v>>>^<v>>v<>>v^v<<>vv>^^vv>vvv<v^vv^^v<<v^>v<<^v^vv<><<v^vvv^v<v>^^>^v^>>^><><<v<vv<v<>^>v<v^<^v><^vvvv>^v^><v<v>v<v>v>^<v^<>>^<v^vv<v><<v>><<<v>^^>^^^>>v<<v><>^vv>^>>^>^v>>>v<><>><v<<v>v>^><^<vv^v^v>>>>>^^^<>v^^<>vvv^><>><<<>v^<^v^^<<>>v^^^^>>v>>>v^^<><^>vvv^>>v^<<><vv<^v>>>>v<vv<<^^^<^>^^vvv^<><<v>>v<^^<vv>>^vv<<^^^^>v<<><^<<>><<>^v>v<><<>vv>^<><vv^vv>>v^><>>vv<^><>><^>^v^>>>^>>v>>^v>v^v>vv<^<>>>><^>>>v^v^<v<>^v^
v^^^vv<>^<>><v>^<^^v^^^<^^<vvvv^<>^v>^><v>v^><v<>^v<v><vv<<<v^>v>v><vv>^v>>><^^^><<vv>^vvv^>^><^^<^v>>><^<>v>^^<<vv^<vv^^^^^^v>><<v<v<vv<^<^vv<><v<vvv^>^^>v<<^^v<>>>>^vv^<^><<v^>v^^<^<^v<<>><^>^<v^vv<<>^><>>^vv^>vv<>>v^v<>><v^<v<v^^v<<v<vv^>>>v<<><^^v<>v<>v>>^vv<v^<v^v<vv^>>v^v<<>>vv<<^>^<<v<v>>^<v^v^^<vv^^^vvv>^^vv^v^^v<v^>^vv<<^<v<^>^^>v>>v<>^>><<<v^^v<^<>v<v^>v>vv^>^>>v>v<<><^>^<<^>v>>v>^vv<<^>v>v<^^><v<v^<v^^v<^vv<^<<<v><v^>>^v^<<>vv><><v><v><><^>^>v^^<>v>>>v<><^>>vvvv<^vv>v^^^>><<<><^vv^^^v^v<>><^>>v^v^><^<^<<v>v<vv^<>vv^v<^>^>v<<<<v>>>v<^^vv>v^v^>^v>><<<v>^vvv<vvv><^<v^^^>^<>v<v>^^^v>v>^^>^>^^^v<>^v^<^v^>^>><<>^v<>v^><>v^>vv^^<^>v^v>^vv^^><^<<<<><>^vv>>>^v^^>v<^><>^<^<<^v>v^vv><><<v<v^>v>><>>^^v^>^^v>><vvv>^^<^<<<>>v<<<^<><>v^vv<vvv<>^^<<>^<<<<^><v<^><>^>>^vv^<>v>^^>v<><<^>><>^v<v^v>v>>>v^^^v^>v><>^v<<><<<><<v><^vv>^>v^<v<v^>>vv^<^><^<^<v><>^>>>v^>^><>^v<vv>><^vv^^<vvv^<vvv^<^<>^>^<vvv>>^<<<^v>v<v^<>^^>>>v<>^v<<^<<^>v>^><^<<vv^v^^v>vv<v<<>^<>><>^^><<v^><^^>v>v><v>>vv<>><<><^<<<v<
^v^^<v>><^><v^vv^<<^^v<>^v<>>^v><^<>>^<>^v<vv<>^vv<^v<v><<^v^^v>^><<<>^v^v><<^<>v^v^vv<<>v^><><v<<v<<<>v^^v^^<>^v>vvvvv^^^<^^>>>v<>^^<^^<><<>>v<vv<<>v>vv>v><^vv^^<^<^<v<<<^<<><><<^v<^>>^v>vvv<^^>>v>>vv<v>>>^<><<<>v<>^vv^><v^>vv^>v<>>>^v>>^<v^<<v>>^^<>v><^v<vv^>v<^^v^v<v^^vvv^^v>>>><vvv><>v>v<^v<^^<<^vvv^^<<vvvv>>><<><><^^<^>><>><<<<<v^^^>v^>>>v>>^<^vv>>><^v<>>^^v^v>^^<^<>v^>^^><v^><^^<v^>>><^>v<<<^^vvv><^^v^<>>v<<<^v<<>>vv<v>^><^<<><v^<v^v^^^v<^>vv>><v>>vv><<<<>^v><^<>vv^vv<^v<^^v^^^^>v>vv^<v>^>^v>v^vvv^<<vvv^<>v^<v<v>>>>><^<v>v>^^v>>^><^^v<>v^v^<<<<>>>^v<>^>>^<vv^v>^^>v^<^>^^>><v>^^^^^<^<^v^>v>vv><vvv^><^<^^><v>>v^v<<>^<<>><v>^^^v<^^<>v^^^>>><<^>><>^>>v<<v<^vvv<<^><v^v<>v<<^>v>v><<v^>>^^<v>>^v^<<><>^^^^><<<>^v<v<<<vv^v^vv^v^<>^v<^^><><vv>>vv>^^>^^^v<><v^v<>^^>^<^v>vv^<<<<v>><vvv^^^^>v^<^^<><<<<^<^v><^<^v><>vv>>v>^>>^v><>><>^>v^>v>v<>^v^^v^>>>>>><v^v>^v^v>v><<^v<vv^<><vv>>^<>vv^v<v<>>>^v<^^>^>v^>><<<vv^v<^v^<^<>^^<>^>v><<<^v^^^^v>>>^^^v><^^v<v>>v^<>^v><v^^>^v<<><^v<^v<>v^v><^^v>^>^v<^<
<^^vv>^<v>^<<v<><^<^>^<v<>v>^^<<>^<^<>>^>^<<^<^v>^>>>vv<^^<<>^><^^<>><<^^>>>v^>^<<^>>vv^><^v><v><vv^>^>>v<><<><<^v<>^^<<>v>^v<^^^<>^^^<v><^<>><<<<<>v^^<<<v<>>^^v<v^^<^<<>^>vv>>v>^><v^>^<><<>v<^v^^v<vv><>vv>v^v>><>>>>^>v<><^>v>v><vv<^^>v>vv^v>v<<>>><vv>^^<<><v^v<<<^>^v<vvv^>><vv>^>^<v<^<>v^<v^v^>^<^^>>^v^<<vv<^<>>v^^>v^><<v<v^<v^<><^<v>vvvv>>v^v^vv>^v>^vv<^>vv<v^<>^v<^<v<>>>>^<>v^^><^<<^vv<^<^v<>>>^<<v>v^^^vv>v^vv<^>>vv<<<^>v^^>^><v^v><<v^<v^vvv<^v<^v<<^<^>>><v><^vv<^<^vv^>^vv<^^vv^<<>>vvv^v^v<^>^vv^v>vv>^^>vv^vvv^v^^>^vv<^^>v>>>>^>v><>><v^v>vv^^^<^><vv>><v^>v>vv^>vv<>^^^<>^^v^>>^^><>v>>>v>vvv<v<<v^v^v^><<>^^^^><<<v^vv><^><>^v^^<<<>><<>><v^<^<><><>>vv<<<v^>^^v>>>^^v<^<^^^^<v^^>vv><>v<^^<>^>>>>>>><vv^^vvv^<vv>>vv>^^v>>^<<^^<vvvv<^<>^<v<^>v>>>^<v<^^<<>v<<^<>vv^<vvv<>>>^>><^>^<vvv<>v<>vvv>>^>^v>^^v<vv<v>>>^^<<>vv>><vv<^<v>^v><^<>^<>^v>^^v<v>v<v<v<<^vvvvv<><^<v^><<>v><<>><<^><^<<^<^v<><^><<vvv^<<^<>v<v<>v>>^^^<>>v>v<^<<>>v^><v<^v><<<<>>^v^v>^^<>>>^<>v>>v><<^>^<v<v<>>^<<>^>vv<^v<>>^>v^>^vv<>
<<>^<>v<^<>^><vv^v<^^v^<<>>>^<<v^<vv^><v^<^>^v>><^>v<^v<<<v<^v>v^v><v<<v<v^<v><^>^^<vvv>v>>v>v>v^<^v^v<<^>^<v>vv<v>vvv^^<v<v^<>><>^<v<<>^^v>>^<<>vv<<v>>>>v^>^>v>vvv>><<<<^v<>><<vv>>^^^vv<^><<><<>>v^>v^<^v<^<vv>^><>v^vv>^^>>v<^>v<>>><^vv^<><v^<>>^><>^>v<>><^<>v^>^^v<<<^v<><^^v^<^^<v^<>>><v<<>^>>>vv<>^<^<>>vv^<v<v^<<<<vv>^^>v>^v^<>v^<^v<><>vv^^<<v<^v<>>^<v<^^>^>v<^>v<v^vvv>v>vv<v^^<<>vv<>v<<^<<<<>><^^<^<^<<^<v^^<>>>>>v^v><>^<>v<^<<vv<>v^^<><^>^v^^^v<^vvv<v<>v>>vv>v<>><>v<<^<>v<>>><v>v>^>v<^v>>v<<>v>>^v>^^<^^<v^vv<>><^^<<^^>v<v^>v^<^v>>^>v^vvv^<>^>vv^vvv>v<>><<<^^v<<^^v>>>^<v<^><v^v>vv^v^<>>v<>^^><^><v^<<<>v><<^^><>>v^^v^v>>>>^^v>^^><v^<>>>^<v>v<v<<>>^v<v>v>v<>^>v>v^v<^^^>><<<>^v<vvvvv><vv^^<^>>^<><><>>>v^><<^>^v^<^v^<<<<<^<v^^>><v<^>v^>v>^v^>^^vv<vv^<<v><<<v>v<><<<^v<v^vv>vv<>>^>^v>><v><<<v^<>^>^<^<^^v^<v<><v<><<^<^^>v^^>v^><^v^<^v^><^^<>^>>v<v<v>vv>>>>vv>><><^v^<<^<^^v^>>vv><^^v>v<>v>vv^<^<<>vv^^><><>>>^<^<^v^<v>^>v^<v<>><>^<>><^>v<<^<vv^>v^^>v^<v><v>>^v>><<v<vvv<<vvv<^<<^v><^<^vv><<>>^
^<^>>><><>vv>>v>v<>>^<^<><>v>v>>vv^^^vv^<^v<<>>^>^^v^vv>vv<v>>><<vv<<v><v^v^^>v<v^><vv<vv^^v>vv<<v<^>v^^>^v>>^v>^><<<<^^>^<vv^<^>v>v^<v>><^v<v<<<<>v^<>><^v<^v>^>>>><<<^^<<v^^<v^>^vvv>v>^^>v>^>>><><>>vv<<><><><>vv>^<v>vv>>v<v^>v^>v<^v>>^^v^<<^v^^v^<v<><v^^vv<^^<<><<v<vvv^<^v<>><>><>^>^^>^v^>>>>><<>^>^v<^<>>^^<>>^^>^v^>v^v><v^v^^><>^^v<^^^^vv^^<^<^<^^^^<>v^v^^><>>>^<>^^v<>^>><<^^<<<<><v<<v><vv<<vv<<^vv<<<^><^><vv^v<<>vvv<<<>v><vv^vv<^>>v<v^>v><><>>v>vv><v<^<<<><>^v<<>>v>vvv<<^v^vv><<v^>><v>v^>v>^v<^v<v<^v<>v><v^^><<^<><^^>^>^v<^<>^^<^>v>v<<vv^^v>^v<>><>>^v><<>vv<>v>v^<<v<>><vv^<vvvv^<>v^^v<^<v><v^v>>^>^>>v^^^>>^>><^vv>><^^><v<vvv>>><v^<v^v>>><<<v>>^^v<<>^^v^<vv>>^>^v>>^^>^>^>>>v><^<><^>^<<<vvvv^>>^<vv<>vvv^vvv^><^<><><v>v<>>^<<^>><vvvv>^v>>^<v<><v<^<>^^<vv<>>^^<^^><v^><>^^^v^vvvv^^^v<vvv<^><<^><vvv>^v<vv<<v^^v<>^^<v^<v<>^v<^>^><>^>><>^v<v^>>vv^^><vv^v^v^v<<>>vv<<<>><>^>vvvv>v^v^v^>v><v<>v<<vvv<<<^><<>v<<<<>v^^^>v>v<><^<<v<<^<>^v>^<v^<^>vvv><<<>^<><^^^^^vv^^^<^<^<v<><^>^vvvv<^<<<^<^<^<>>v
<^<<v>^>v^>v^>^v<><><<^>v<>v><v^v^<>>^^^^v<>^^<<^<>>vvvvv><vv^>vv>v^>^<>v^v>^^>v^vv^>vv^<>^>>^^^^vv<<v><<<v<v>^<<^>^>^v><<v<v^^^><>><>v<v<><<v^^>v<<^v^><>^>^><v<<^^v^<v<^><v<>>^^v<v^>>^^>^<<<^>^^vv<<>v<<v<<^v^>v^><v<<<^<><<^<v>v^vv<<v<vv<>v<v^^>^><>>>>>^<>><><^><v>v<^^^>^<^>vv<^<<v<v^vv>v^>vv^^>>^^>^>^><<<vv<>^vv^^>v>v<<>^^^<<^^>v><<^><>^<^>v<<^v<>v^>^vv^^<^^<>^<>>^vv>>>>>v>vv>>>^<<v<^^><<<<^<v^<^v^>>>vv>>v<v><<>^<^<<^v^>>^^v<^>v<v><v><v^^vvv>>v<>><>^v<v>^v<>^v<><^v<^<v<^>^v^<>^v>>>vv^^>^>vv^v<^v^>^vv>>^<<>v^v>vv^>>v>^v<v^<^^v^v>vv^<^<<<v>v><<v><^>^v^v^<<v^^^<v><>^v^^>v>^<<>^<<^>^>v<<^^^>v>^^v<v<^v<<v<vvv>^>^><<>^^v>vv<>vv^vv<>>^^^<^vv<v>^^>><>^vv><>>>^>^^v^><>v^v^<^<^<vv><><^^v><^^^><<v>v<<v>>v^>^><><^<<^v^<v>v<>>^^<<><>vv^>^^^<<>^<^vvv>vvv^v>>^^<<vvvv^<<v^<v>v<vv>^^>^>v<^^v<<>v><>^<>v^^^<vvv<>^^v><<v>v^<^v<v>^^^<^><^v<<vv>>>>^v^^<<>><vv><><>v>^<>>v>><>^vv<vv><vvvv<>>^<^<^>>^v^>^v>v<>v<><>><v<vv<v>v^>v<^>>v<<v^^>v><^>^>v<>>v<^<>vvv^v<<v<v^vvvv><v<^>^v^^^v>^><v^^^vvv<<vv>^<<^<<>v^v>^^>
><v^^<^<^vv^>>v>>^>v^<>^^vv><>><^v<<<>^>><^<>>^^<^><<<<>>^^>v^v>v<v^^v<^v^v><v^<>v<v^<<^<<^v>>v>^v<vv>v>><^^>v>><<^<vv^v>><><<v<^vvv>>^v^^vv<>>>><^<^><>v<^^><<<<>>v^<<><^^vv^^v^^<^><<v>vvv<^<vv<><^vv^<vv>v>>v>><v<>^>>vv>v^<v<<<v^>^<>vv<v^>vv<^^><^<><^>^^>>>>^>>>^<vv<<v>v><<^v^^><><><^>>><>v>v>^>v<<<>v<v<v^^<><>v>^v<>^<<<^v>>v>v><<>^>^<>v<^^>^^v^<>^<<vv<<^>>v^><v>^>><^v^vv>^^<v>^<v<<^<^^>^^v<v>v><v<<>>>^^>><>v<>v<^>^v><>vv<<<v>^v<>vv<v>^v^>vv^><^vvvvvv^v<v>v<>^>vv>v>><>^v^v>v<^<^^<vvv<^v<^>^<>^^v^^<<<v>>vv^^>^<>>>>^<v><>^^<vv>>^v<<<>>v>^<^>vv><v^^><v>v^>><v<<^^<>v><vvv<v^^v>^^v>^^vv^>v><>v<^><v<v<^><<><<<<^<>^<><v^v<v>vv>^^>>v<^vv><^<v^<^<v^v^v><^<>v^v<><>^^>>>v^>>>>v>>^<^<^vv>v^vv>v^<^<><^>>v>^<<><^<v<<v<<<^>vv<^>^<>^>>v<^v><<^<<vvv<><^<<<^>^<<^^<>vv<v<<>vv^<^v^<<<>><^v<v<<<<v>^^^<<<vvv><><<><v>>vv^^v<v<v<^v<<>^^<<>><^v<<<<<>v>^><^>>v^^>^^<<^<^^^>^>^>^><v>v^^<><^<<<>^<^>^<<<>>v^vv<<^v<^>>vv<<v^v<v^v>^v><>^>vv<^v>vv<><<>v<v<vv<^v>^^>^v<^<^>^^v^>v><vvvv><^<^>>>><^^<>^^<<^vv^^v<^>v^v>>vvv
<<^<v<^>><<><^vv><<<v^<^^^vv<>v<^vv>^v>^>vv<<v>^vv^^v>^v>^>><v^>^^<^^v^<^vv<>v^<<^^<<v^^<^^><v<<>vv<v<<v<v<v<<>^<v>><<^<v<>^vv^v<vvv<>^<<<^^><v^v>><vv^v^<v<^<<^^^v^^vv>>^^>^vv>^^vvv<^<<v<v<<vv<^vv>^>^^^<<><vv><><^v<^^>v^v<^>^>v<v<v>^<>^<>^><<v><v>>v<vv^vv<^v<>><^><^^>><><<>^^v>>>>v><v^>vvv<>>^^^^<>^>^v^v^^^><^^^v><>v<v<v<>^<^^^^<>v>v<<v^>^>>^<<<^<<^>>>><^<v<<^>vvvvv>>>^<^v>>vv^>v<v<>^vvv>><^^<<^<<>^>^^<vv>>^<^^v>v>^vv><>v<v>v^<><<^v><vvv<v^<<>^^vvvv<<^^v>v<^<v<^<<<v>^v><v<^^^>>v<^^v^v^v<v^^v^^^<^><^v^>^>vvvv^v^vv><>v^v^^<v^<<^^<><<v<^v><>^>>>v<><<><^<^^^><^<vv><<><v^vv>^^v>>>>^v^<^>^^>><^>>^v<^v><>>v>><^^>>><<<<^^<<v<^<>vvv^^<vv<>v>^>>^><<<^<^>v^>v^^><<^>^^^v<<^<v>v^>^vv^^vv^<^>>v><v>^<^v<<>^<v<^<<^^>^>v^><>^<<^>^v^vvv^^^^^v^v<^v<v<v^^>>^>vv<^<v^v^vv>>^>^>v^^<^^^>^><^><<><v<v<vvv^^>v^<>^^v>>vv<v><<<>><>v>^<^^>v>vv^vv<<^v<<v>><v^^v^^<vvvv>^^^>><<><<^^><vvvvv<v^>v<^^><><><<^>^^<v<^v^vvv<v>v>^v<<>>v^^>>><>>v^v<>v<>><><<^^^v^<<^<v^<^<<v<^^v^<v^><v>>v<>^><^^^v^<^<<<^v<^<v<>vvvv>v>>>^vvv<v<>
v>^<^>^>^<<>^^>^^v^vv>>><v>vvv<^^<^v><>>^^v><v<<v<>vv<^v>>v><>vvv>v>>>v<v>vv<v<v^^>^vv>v<^>vv<v>v^><^<<v^><^v<v<<^><<v>^^>>><v<>>v>vv<^<<<^><v>>>v^<v^<v>vv><^^v<<><<<^^<<v<<><>^v^v<<v<v^><^>v<^v><^>^>><<>^^>^><v>^v<<^^>^^>>v>v>v<^^v>^>v>^vvv><<^<v<>vv<^<vv^><v^^^^v^<>^v^v<><v>vv<>vv<v<^<>^v>^v^<vv>>^<^<<^^^vv^><vvvv><vv^^>><v^<^v^^<^<v^>^><><<^vvvv<><<>^^><<<^>vv<^v>v>><<>vv^^<^v<<><v<>v^<<>^<vv^^><<^v^>>><>v^>^^>>vvv>v>><<v^vv^<><v^>>v<v<<<<<><^>vv<<>^^v<>>><^^<>vv^<v^v><v<<>>v^vv<>^>v<^v<<v><>v>vvv>v>^>^<v><<^v>v^^<^>^><vv^>^>><v>>>>v<<>^<>v^^<<><>^<vv<>^v^^^^<^v><^<<^<>^^^<^>^>v^^v^^<>^vv>><><>^^<<>v<v^>vv^>^vvv><v>v>^vv>v<>vv<v<><<v<^<<<v><<><^>>vvvv<^^<^v^<<^<><v^^^><>v^^v<<v<<>^>^v<^<<v^<^^^<>><^><<<<>v<v><^v>v><>v<vv><<^<^>^v<>v^>>vv>^v><^<>>><^v^<^^<>v^v^<<<^v<><v><>v^vv^vv>v^>>v<>>><>^><vv^<^<><<>v<v>>v><<>^^<vv<v^v<v>v<v<^v<<v><^v^vv>^vv^>v^^^^^^v>>^v<<<<v<<v>vvv<^vv^v^>^>>v>>><>v<vvv<v^^v<vvvv<^^v<^>v>>v^<^^<<<v^v>vv>v^<><^>><<<>><v><>^>v<^<>v^^>>>v<<^^v^<^^<>><^>^>^^>>><<v^
v>>^^>^><^<^>v><<>^>^<^^v<>^>v<>v<<v>><^v>v<>v^<v>^vv>>vv<^^v>vvv<vv^<^vv^<v<v^^^>>v^^v>^vv<>^<<<<^>v<v^v><^>>><^v><v^<v>v>><v>>v>>v>v>^<>^<^^v>^>><v>v^v>vv<v^<v^^v<v>^><^>vvv>^>>v^v^<<<>^<v<^>^v^^<<vv<<<>^<<<>vv>vv<v>^^<^<>vv^>v<^^^v<<^<^<><>^vv^vv^><vv<>vvvvv^<^^^v^^<<^^<>^^<<<>^v^>v><>>>vv<v<>><v^v^><^^>>vv>>^<^^<^v>^>^<><^v^^<^vv>v<<v>v^<^<^vv<><v>v<v^v><<>>^v<<^<v^<>>>vv^^<<<v^<<>v>^<><<>vv><^^v^v<^^^<v^><v^>^^><^>vv<v<>><v<>^^^^vv>^<<^<^>^v>^^^v>>v<v>v^v<><>^<^><>><><^>^<v>^><<>>vv^>>><^v<<^^>^^><>v<<^>>v<<^vv^>>><<>vv<>^^<v>^^^<^v>v^^vv>^^^<^^^vv>^^v>vv>^v^>><v><^>>v^^<v^^<<vv^^<v^^^vv<<>v>><><vv^<>>^v>v>^<>vvv^<vv>^v<^>><>v><>>v^<<v<>^<<>^^<<^^>vv^^<>^>^<<>^<v>vv>><<>^v><<<><^^^v^^><<v<<><v^^^>><v<<<^>^>><v>>>v^><<><<^v<^v<>v>><^>>>^^v^<v><v>^^<v>>^<>^^^^>>v<<<^^^vv<^<<^^v^^<^v^<^v<><>>>^<^^v<<v><<vv^>v>v^>><v<<<<>>v>^<<v^^>>^>^<^>><v^<>v^v^^^>><>><><><^^<<>>>>>vv>>^<><^<><><<<>^><v>vv<v><^v<^^<^v^>vvv^>v^>>><<^^^><vv<<>><^><^<><<^<<v^^<>vv<^v>><<^<>^^<>vv>v<>^>>vvvv^>^v>v><>^v
><^<^v^^<>vv><v^^v>>v<^v>v^v>v>v^^>v^<v>v<>^><v><^>>^><v>>^v<>v^^v>^vvvv<<v^>v^>v^<>>^^vv<<>v^v^<>v><<vv>>>>>>^^>>^v^>^<>><v>v>>^^^v^<v><^^^^v>vv^<^>^v>><^<<><v>v>v^>^>^v>^><>vvv^v>>^vv^>^vv^^^^v>vv<><>>>^<^^>>^><<<><>^><>^^v<>v^><^>v>>>^><v^>v^v<v><v<<<>vv^^<>v^^^>^^^^>>>>>v<v^v^^^^v>^>vv>^<^>^v><^^><^v>v>^<>^<vvvv>^>v<^v><v<<^v^<^^^<vv>vvvv<>^v<><v^<v^<<^v>^<^<^v>^>v<v^<v>>^^>^vv>^^<<v^vv>>>v>^<^<<^>v><>>>^vv<<^><>>v^>^<>^v><v>>>^<<v>vv>>^^v<^><^vv>^<>v>^<v<^<><>^<^>>>>>><<>>v>>v<<^>^<>>^<^><^>^<^^^<>>v<>^^><^>>vv<v^vv>>>>><^<><<<^^><^^vv>^v^<v^<<^>>^<^>>^>><<^>v<^^>v<v>v^>^>v>^v^vv^>v>^^>>v<>^>>v>>v<<v^>>>^^<^v<<>>><>>vv<^>^^v<vv>vv<v<^<v><>^v>v^v<v>><>v<^<v^v<<>v^v>v<>>^v<v^v^^<vv^>>^^^^vvv<<^v>><^^>v^<v^<>^<v^<<<v>^v<>><<v^v<v>^>^v^vvv<>v>^>>>v<<<v<v<<^v<>>v>^<><v<<<^v><>>^>v<v^>v>v>^^v>^^<^^^<vv^>v<<^<^<v<^^^<v<^v^^v^^^vv>v<v>v>v^><>>^v>v^<^^^vvv>v>vv>v<vv>^<v>>>^v^<>v<>><<<>>^v^^^<>><>>v<>v<<<^>v^><v<^>v<^<<<><^<<<v^>>^<v<<>^^v><<>><vv^><<^<><^><>>^>^^<v<<^vv<^>>vv<><^v^v>^<v<v<
v>><^>^<<>>>^v^<vv>^v>^v<^<><vv>^<<v>>^><v>^vv><v>>^<^^vv^<vvv>^^<v<^v<>^>^<^<<vv>>>^>vvv<<^v^><^v<>vv>^>v>^><v>vv<vvvvvv<>vv^><><^>^v^<<v<^^vv^^^>>><^<v>^^><<>v<<^<v>^^<^<><^v<v<^<v>>^<<^^v^<><>vv^v^^vvv^^^><vv><<^^<>>^<^v^vvv<^vvv^v^^>^v^^<^v>^vvvv>^>v<<>>>v>^v<><^^^^^<^<vvv^^^v>^<^v^<>><<<><v<<^<vv>>^>^^v^^><<<^^vv^<^<^<<v>^^<>vvv>v<vvv>^^v><>v>>v^><>>>><>vvv^<<^<>>><v<^v<<>>^<v<>>v<<<v<>^^^v^^^>^<<<^vv<^><v>>><^<v><^<v^>v^<^v^>>v<<v^>^^>^^v^^^^^>^>v^v^vv^^>v^v<vv>>>^vvvv>^<<<<>v<>v<>v^>>><v<v^^<>>v<^vv>v^>><<>vv^^v^v>v>v<>v<>^>>vv^<>v><<v^vv>^>>vvvvvv<v<>vvvv^^v<<<v<>^>^>>>>^><v^>><^v>><v^vv><<<v>^v^^<^vvv^^v<v^<vv<v<^v^vv^v>v^>><v>vv>^>v^v<v<^v>v>v<<<vv><>vv^v>^>v^^v^<vv>v>>^vv<><vv<v^>v^v>>^<>^^><v>>>>vvv<v<vv>v^v>v^>><vv><<>>^<<<>v>^v^><><^>^^^<>v^^^>^><^v>^^v^<>>>><<^>v>v><^v<<^>v<<<>^>^^^<>>v><<v^^><^<^>><<v<>^v^v^<<>>>v^><<v<v>^v><>v^v^><<v^>><v<<^>>v<>v>^v><<<>^><^v<^^<^<^>vv^><^<v<v>v<^>vv>><v<>v><<^>vv>^<^>^vvv^vv<<<><<>vv^v^^vv^vv<^><<>v^<vv>v<><>v>^><<><<v^^^^v^>>^>>^v^v
"""
def print_grid(grid, move=None):
    print(f"---move: {move}---" if move else "Initial State")
    for row in grid:
        print("".join(row))

def get_solution(warehouse: str, moves: str):
    # First, parse the warehouse into a grid
    grid = []
    robot_location = None
    for y, line in enumerate(warehouse.splitlines()):
        grid.append(list(line))
        if "@" in line:
            robot_location = (line.find("@"), y)
    for move in moves:
        # print_grid(grid, move)
        x_modifier = 0
        y_modifier = 0
        if move == "^":
            y_modifier = -1
        elif move == ">":
            x_modifier = +1
        elif move == "v":
            y_modifier = 1
        elif move == "<":
            x_modifier = -1
        # We should be gauranteed to be in bounds since there is a wall
        next_x = robot_location[0] + x_modifier
        next_y = robot_location[1] + y_modifier
        next_square = grid[next_y][next_x]
        if next_square == ".":
            # If the next square is open, 
            # First mark the current location as being open
            grid[robot_location[1]][robot_location[0]] = "."
            # Then, move the robot location
            robot_location = (next_x, next_y)
            grid[next_y][next_x] = "@"
        elif next_square == "#":
            # If we're at a wall, stay at the same location and go to next move
            continue
        elif next_square == "O":
            # If the next square is a block, try to move
            space_after_block = grid[next_y + y_modifier][next_x + x_modifier]
            blocks = 1
            while(space_after_block == "O"):
                blocks += 1
                space_after_block = grid[next_y + (y_modifier * (blocks))][next_x + (x_modifier * (blocks))]
            if space_after_block == "#":
                # If we're at a wall, we can't move anymore, so continue to next move
                continue
            elif space_after_block == ".":
                # First, move the robot
                grid[robot_location[1]][robot_location[0]] = "."
                robot_location = (next_x, next_y)
                grid[next_y][next_x] = "@"
                # Then, move the blocks
                for i in range(blocks):
                    grid[next_y + (y_modifier * (i + 1))][next_x + (x_modifier * (i + 1))] = "O"
    coordinate_sum = 0
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "O":
                coordinate_sum += ((y * 100) + x)

    return coordinate_sum


# print(get_solution(warehouse_actual, moves_actual))

def get_solution_p2(warehouse: str, moves: str):
    # First, parse the warehouse into a grid
    grid = []
    robot_location = None
    for y, line in enumerate(warehouse.splitlines()):
        row = []
        for char in line:
            if char == "#":
                row += ["#", "#"]
            elif char == ".":
                row += [".", "."]
            elif char == "O":
                row += ["[", "]"]
            elif char == "@":
                # need to take current length into account
                robot_location = (len(row), y)
                row += ["@", "."]
        grid.append(row)
    print_grid(grid)
    for i, move in enumerate(moves):
        x_modifier = 0
        y_modifier = 0
        if move == "^":
            y_modifier = -1
        elif move == ">":
            x_modifier = +1
        elif move == "v":
            y_modifier = 1
        elif move == "<":
            x_modifier = -1
        # We should be gauranteed to be in bounds since there is a wall
        next_x = robot_location[0] + x_modifier
        next_y = robot_location[1] + y_modifier
        next_square = grid[next_y][next_x]
        if next_square == ".":
            # If the next square is open, 
            # First mark the current location as being open
            grid[robot_location[1]][robot_location[0]] = "."
            # Then, move the robot location
            robot_location = (next_x, next_y)
            grid[next_y][next_x] = "@"
        elif next_square == "#":
            # If we're at a wall, stay at the same location and go to next move
            continue
        elif next_square in ["[", "]"]:
            blocks = 1
            # If the next square is a side of a box, attempt to move it
            if move in ["^", "v"]:
                # If moving up or down, we need to check all of the squares affected
                next_range = None
                if next_square == "[":
                    next_range = range(next_x, next_x + 1)
                else:
                    next_range = range(next_x - 1, next_x)
                for i in next_range:
                    if grid[next_y + y_modifier] == ".":
                        # We're good?
                        ...
                    elif grid[next_y + y_modifier] == "#":
                        # can't do the move
                        continue
                    else:
                        # Otherwise, we've hit another box
            elif move in ["<", ">"]:
                # If moving left or right, it should be pretty simple, as we won't have
                # any overlap. Check 2 ahead until the space is empty or a wall
                space_after_block = grid[next_y][next_x + (x_modifier * (blocks * 2))]
                while space_after_block in ["[", "]"]:
                    blocks += 1
                    space_after_block = grid[next_y][next_x + (x_modifier * (blocks * 2))]
                if space_after_block == "#":
                    # If we're at a wall, we can't move anymore, so continue to next move
                    continue
                elif space_after_block == ".":
                    # First, move the robot
                    grid[robot_location[1]][robot_location[0]] = "."
                    robot_location = (next_x, next_y)
                    grid[next_y][next_x] = "@"
                    # Then, move the blocks
                    for i in range(blocks):
                        start_x = blocks * x_modifier * 2 # the distance from next_x to start at
                        to_insert = []
                        for x in range(blocks):
                            to_insert += ["[", "]"]
                        if move == "<":
                            grid[next_y][next_x + start_x:next_x] = to_insert
                        else:
                            grid[next_y][next_x + 1:next_x + start_x + 1] = to_insert
            
        print_grid(grid, move)
        if(i == 10):
            exit()


    coordinate_sum = 0
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == "O":
                coordinate_sum += ((y * 100) + x)

    return coordinate_sum


warehouse_3 = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######"""
moves_3 = """<vv<<^^<<^^"""


warehouse_4 = """#######
#...#.#
#.....#
#.@OO.#
#..O..#
#.....#
#######"""
moves_4 = """>>v"""

print(get_solution_p2(warehouse_4, moves_4))