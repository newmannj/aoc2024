import re
from typing import List, Tuple

# Part 1
total = 0
with open("memory.txt") as file:
    for line in file:
        matches: List[str] = re.findall("(mul\(\d{1,3},\d{1,3}\))", line)
        for match in matches:
            nums = re.findall("(\d{1,3})", match)
            total += (int(nums[0]) * int(nums[1]))


# Part 2
# Take do() and don't() into account :grimace
total = 0
enabled = True
with open("memory.txt") as file:
    for line in file:
        matches: List[Tuple[str, str, str]] = re.findall("(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))", line)
        for match in matches:
            if(enabled and (not match[0] == "")):
                nums = re.findall("(\d{1,3})", match[0])
                total += (int(nums[0]) * int(nums[1]))
            elif(not enabled and (not match[1] == "")):
                enabled = True
            elif(enabled and (not match[2] == "")):
                enabled = False
print(total)

