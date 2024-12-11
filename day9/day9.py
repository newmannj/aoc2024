# Digits alternate between indicating the length of a file and the length of free space
disk_map = None
with open("disk_map.txt") as file:
    disk_map = file.readline().strip()
# disk_map = "1110101010101010101020"
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

# Now we need to calculate the checksum
checksum = 0
for i, x in enumerate(arranged_blocks):
    if x == None:
        break
    else:
        checksum += i * x
print(checksum)
