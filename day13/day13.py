machines = []
with open("test_input.txt") as file:
    machine = {}
    for line in file:
        if "Button A" in line or "Button B" in line:
            moves = line.split(":")[1]
            split_moves = moves.split(",")
            x_move = split_moves[0].replace("X+", "")
            y_move = split_moves[1].replace("Y+", "")
            machine["button_a" if "Button A" in line else "button_b"] = { "x_diff": int(x_move), "y_diff": int(y_move)}
        elif "Prize" in line:
            location = line.split(":")[1]
            coords = location.split(",")
            x_location = coords[0].replace("X=", "")
            y_location = coords[1].replace("Y=", "")
            machine["prize"] = { "x": int(x_location), "y": int(y_location)}
            machines.append(machine)
        else:
            machine = {}

print(machines)