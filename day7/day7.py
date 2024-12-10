from typing import List

# Part 1: Determine if options can be combined with + or * to get to test_value
def can_combine_to_value(options: List[int], value: int, acc: int):
    # Base case. We've evaluated all options, and 
    if len(options) == 0:
        return value == acc
    first_option = options[0]
    return (
        can_combine_to_value(options[1:], value, acc + first_option) |
        can_combine_to_value(options[1:], value, acc * first_option) |
        can_combine_to_value(options[1:], value, int(str(acc) + str(first_option)))
    )

total = 0
with open("calibrations.txt") as file:
    for line in file:
        test_value = int(line.split(":")[0])
        options = [int(val) for val in line.split(":")[1].split()]
        if(can_combine_to_value(options[1:], test_value, options[0])):
            total += test_value
print(total)