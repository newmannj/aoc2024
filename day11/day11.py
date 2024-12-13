from typing import List
test_stones = [0, 1, 10, 99, 999]
test_stones_2 = [125, 17]
stones = [5,62914,65,972,0,805922,6521,1639064] 
def apply_blink(stones: List[int]):
    x = 0
    while(x < len(stones)):
        stone = stones[x]
        if(stone == 0):
            stones[x] = 1
        elif(len(str(stone)) % 2 == 0):
            # TODO: Handle the split
            stone_string = str(stone)
            half_string = int(len(stone_string) / 2)
            first_half = stone_string[0:half_string]
            second_half = stone_string[half_string:]
            stones[x] = int(second_half)
            stones.insert(x, second_half)
            x += 1
        else:
            stones[x] = stone * 2024
        x += 1
    return stones

# OOF. Doing this efficiently seems to be the problem here
# Could we do DP? Where we store a lookup each time
# for i in range(75):
#     apply_blink(puzzle)
#     print("After blink: ", i)

# print(len(puzzle))

# Wait maybe we can do it recursively?
for i in range(25):
    stones = apply_blink(stones)
    print("after i: ", i)

print(len(stones))