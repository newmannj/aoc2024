results = {}
gates = []
with open("input.txt") as file:
    for line in file:
        if ":" in line:
            vals = line.split(": ")
            results[vals[0]] = int(vals[1].strip())
        elif line == "\n":
            continue
        else:
            gates.append(line.strip())

x_input = ""
y_input = ""
for key in reversed(sorted(results.keys())):
    if "x" in key:
        x_input += str(results[key])
    elif "y" in key:
        y_input += str(results[key])
    
print(x_input)
print(y_input)


while(len(gates) > 0):
    gate = gates.pop()
    inputs = gate.split(" -> ")[0].split()
    if not inputs[0] in results or not inputs[2] in results:
        gates.insert(0, gate)
        continue
    result = None
    if inputs[1] == "OR":
        result = results[inputs[0]] | results[inputs[2]]
    elif inputs[1] == "AND":
        result = results[inputs[0]] & results[inputs[2]]
    else:
        result = results[inputs[0]] ^ results[inputs[2]]
    output = gate.split(" -> ")[1].strip()
    results[output] = result

ordered_keys = reversed(sorted([key for key in results.keys() if "z" in key]))
binary = ""
for key in ordered_keys:
    binary += str(results[key])

print(binary)
print(int(binary, 2))

# 1100011101111101101111100100101110001011001110
# 1100100010000001101111100100101110001011001110



    
    

        