import math
locks = []
keys = [] 
with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]
    x = 0
    while x < len(lines):
        if len(lines[x].strip()) == 0:
            x += 1
            continue
        else:
            acc = lines[x:x+7]
            if acc[0] == "#####":
                locks.append(acc)
            else:       
                keys.append(acc)
            x += 7

lock_heights = []
for l in locks:
    result = [None for _ in l[0]]
    for y, r in enumerate(l):
        for x, c in enumerate(r):
            if c == "." and result[x] is None:
                result[x] = y - 1
    lock_heights.append(result)

key_heights = []
for k in keys:
    result = [None for _ in k[0]]
    for y, r in enumerate(k):
        for x, c in enumerate(r):
            if c == "#" and result[x] is None:
                result[x] = 6 - y
    key_heights.append(result)

pairs = 0
for l in lock_heights:
    for k in key_heights:
        failed = False
        for x in range(5):
            if (5 - k[x]) < l[x]:
                failed = True
                break
        if not failed:
            pairs += 1
        # else:
        #     print(l, k)

print(pairs)
        

    
        
         