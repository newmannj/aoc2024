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
    rule_breaker = False
    print(update_list)
    while(i < len(update_list)):
        # Maybe we can fix the list in-place as we search?
        curr_page = update_list[i]
        rules = rule_dict[curr_page]
        # rule_breakers = set(update_list[i+1:len(update_list)]).difference(rules)
        rule_breakers = [page for page in update_list[i+1:len(update_list)] if page not in rules]
        if (len(rule_breakers) > 0):
            rule_breaker = True
            # If the current page is breaking a rule, it needs to be
            # put further down. Remove it.
            update_list.remove(curr_page)
            # Then, insert it right after the last page that breaks the rule
            last_rule_breaker_index = update_list.index(rule_breakers[-1])
            update_list.insert(last_rule_breaker_index, curr_page)
            # print("update_list after fix: ", update_list)
        else:
            # We should only keep iterating if we don't have a broken rule
            i += 1
    if rule_breaker:
        sum += int(update_list[floor(len(update_list)/2)])
print(sum)
        