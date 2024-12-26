connections = []
with open("input.txt") as file:
    for line in file:
        connections.append(line.strip())

m = {}

for c in connections:
    nodes = c.split("-")
    left = nodes[0]
    right = nodes[1]
    if left in m:
        m[left] += [right]
    else:
        m[left] = [right]

    if right in m:
        m[right] += [left]
    else:
        m[right] = [left]

sets = {}
total = 0
for comp, conns in m.items():
    for c1 in conns:
        for c2 in conns[1:]:
            if c1 in m[c2]:
                if comp[0] == "t" or c1[0] == "t" or c2[0] == "t":
                    sets["".join(sorted([comp, c1, c2]))] = True


print(len(sets))

