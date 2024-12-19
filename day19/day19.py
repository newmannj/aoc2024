from typing import Dict, List

available_patterns: Dict[str, bool] = {}
desired_patterns = []
with open("19_input.txt") as file:
    patterns = file.readline().split(",")
    for p in patterns:
        available_patterns[p.strip()] = True
    for line in file:
        if line.strip():
            desired_patterns.append(line.strip())
dp = {}
def solve_pattern(pattern: str):
    if pattern in dp:
        return dp[pattern]
    
    result = 0
    if not pattern:
        result = 1
    
    for towel in available_patterns.keys():
        if pattern.startswith(towel):
            result += solve_pattern(pattern[len(towel):])
    dp[pattern] = result
    return result
    

solved = 0
p2 = 0
for pattern in desired_patterns:
    if solve_pattern(pattern):
        solved += 1
    p2 += solve_pattern(pattern)

print(solved)
print(p2)
