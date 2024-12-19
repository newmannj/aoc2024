from typing import TypedDict, List

class Button(TypedDict):
    x_diff: int
    y_diff: int

class Pos(TypedDict):
    x: int
    y: int

class Machine(TypedDict):
    button_a: Button
    button_b: Button
    prize: Pos

machines: List[Machine] = []
with open("input.txt") as file:
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


# Idea 1: Keep subtracting the more expensive button (a) until the result of prize
def get_button_presses(machine: Machine):
    prize = machine["prize"]
    button_a = machine["button_a"]
    button_b = machine["button_b"]
    a_presses = 0
    # Keep hitting button A until both positions are divisble by button B
    while((not prize["x"] % button_b["x_diff"] == 0) or (not prize["y"] % button_b["y_diff"] == 0)):
        prize["x"] -= button_a["x_diff"]
        prize["y"] -= button_a["y_diff"]
        if (prize["x"] < 0 or prize["y"] < 0):
            # If we have passed 0, then it isn't solveable
            return None
        a_presses += 1
    # At this point, both locations of prize should be evenly divisible by both x
    # and y diffs of button b. Simply divide the positions by the diffs.
    # We should only need to do one here.
    b_presses = prize["x"] / button_b["x_diff"]
    if(a_presses + b_presses > 100):
        return None
    return int((a_presses * 3) + (b_presses))

total_tokens = 0
for machine in machines:
    machine_tokens = get_button_presses(machine)
    if machine_tokens is not None:
        total_tokens += machine_tokens
print(total_tokens)