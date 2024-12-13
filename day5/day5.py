from typing import Dict, List
from math import floor
rules: List[str] = []
updates: List[str] = []
read_rules = True
with open("page_updates.txt") as file:
    for line in file:
        if line == "\n" and read_rules:
            read_rules = False
        elif read_rules:
            rules.append(line.strip())
        else:
            updates.append(line.strip())

"""
Keep rules as dict:

{
    number: [number]     key is page, value is list of pages that must come after
}

Then, when iterating through each update:
- for each page, get the intersection of the pages after, and the rules
- if there are any values left over, the update is not allowed
"""
rule_dict: Dict[str, List[str]] = {}
for rule in rules:
    rule_split = rule.split("|")
    page = rule_split[0]
    page_rule = rule_split[1]
    if page in rule_dict:
        rule_dict[page].append(page_rule)
    else:
        rule_dict[page] = [page_rule]
    
sum = 0
for update in updates:
    update_list = update.split(",")
    i = 0
    passes = True
    while(i < len(update_list)):
        curr_page = update_list[i]
        rules = rule_dict[curr_page]
        # print(f"rules for curr_page ({curr_page}): {rules}")
        rule_breakers = set(update_list[i+1:len(update_list)]).difference(rules)
        if (len(rule_breakers) > 0):
            passes = False
            break
        i += 1
    if passes:
        sum += int(update_list[floor(len(update_list)/2)])

# Part 2
sum = 0
for update in updates:
    update_list = update.split(",")
    i = 0
    passes = True
    while(i < len(update_list)):
        curr_page = update_list[i]
        rules = rule_dict[curr_page]
        if(update_list[i+1] not in rules):
            # Do a swap
            to_swap = update_list[i+1]
            update_list[i] = to_swap
            update_list[i+1] = curr_page 
        