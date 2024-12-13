from typing import List, Optional
# Digits alternate between indicating the length of a file and the length of free space
disk_map = None
with open("disk_map.txt") as file:
    disk_map = file.readline().strip()
# disk_map = "2333133121414131402"
id_number = 0
is_file = True
arranged_blocks = []
for x in [int(x) for x in disk_map]:
    if is_file:
        for x in range(x):
            arranged_blocks.append(id_number)
        id_number += 1
    else:
        for x in range(x):
            arranged_blocks.append(None)
    is_file = not is_file

# Then we need to compact everything
# Note: Will need to take double digits into account
def rearrange_blocks(arranged_blocks):
    head = 0
    tail = len(arranged_blocks) - 1
    while(head < tail):
        if(not arranged_blocks[head] == None):
            head += 1
        # Or tail is not a number, continue
        elif(arranged_blocks[tail] == None):
            tail -= 1
        else:
            # Otherwise, we should be able to move tail
            to_move = arranged_blocks[tail]
            arranged_blocks[head] = to_move
            arranged_blocks[tail] = None
            tail -= 1
            head += 1
    return arranged_blocks

# Now we need to calculate the checksum
def calculate_checksum(blocks):
    print(blocks)
    checksum = 0
    for i, x in enumerate(blocks):
        if not x == None:
            checksum += i * x
    return checksum
# print(calculate_checksum(rearrange_blocks(arranged_blocks.copy())))

id_number -= 1
# Part 2: Moving the whole file at once
def rearrange_blocks_p2(blocks: List[Optional[int]], id_number: int):
    # To start, find the first index of the current id_number
    while(id_number >= 0):
        i = blocks.index(id_number)
        file_length = 0
        while(i < len(blocks)):
            if(blocks[i] == id_number):
                file_length += 1
            else:
                # When we are getting a different number, we know we're at the end
                # of the file.
                break
            i += 1
        # Now we know the file length, we need to find free space to the left
        # We kindof have to start at the top
        head = 0
        i -= file_length
        while(head < (i)):
            if(blocks[head:head + file_length].count(None) == file_length):
                # We can move the file here!
                for x in range(file_length):
                    blocks[head + x] = id_number
                for x in range(file_length):
                    blocks[i+x] = None
                break
            else:
                # If there isn't enough space, try the next head
                head += 1
        id_number -= 1
    return blocks
print(calculate_checksum(rearrange_blocks_p2(arranged_blocks.copy(), id_number)))