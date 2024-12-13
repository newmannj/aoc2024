from typing import List
reports: List[List[int]] = []

with open("reports.txt", "r") as file:
    for line in file:
        report = line.split()
        reports.append([int(x) for x in report])


def report_is_safe(report):
    # A report is safe if:
    #   1. All levels are either increasing or decreasing
    #   2. Any two adjacent levels differ by at least one and at most 3
    # First determine whether the levels are increasing or decreasing
    first_level = report[0]
    second_level = report[1]
    decreasing = True
    if first_level < second_level:
        decreasing = False
    if first_level == second_level:
        # Levels must differ by at least 1
        return False
    report_i = 1
    prev_level = report[0]
    while(report_i < len(report)):
        curr_level = report[report_i]
        diff = prev_level - curr_level
        # If we are decreasing, the diffs should be positive
        report_i += 1
        prev_level = curr_level
        if decreasing and diff >= 1 and diff <= 3:
            continue
        # If we are increasing, the diffs should be negative 
        elif not decreasing and diff >= -3 and diff <= -1:
            continue
        else:
            return False

    return True


safe_reports = 0
for report in reports:
    safe_reports += 1 if report_is_safe(report) else 0
# Part 1: Safe reports
print(safe_reports)

# Part 2: Safe reports with problem dampener
# Just brute force it. For each unsafe report, try removing each page to see if it is ever safe

safe_reports_v2 = []
for report in reports:
    if (report_is_safe(report)):
        safe_reports_v2.append(report)
    else:
        for x in range(len(report)):
            if (report_is_safe(report[0:x] + report[x+1:])):
                safe_reports_v2.append(report)
                break
print(len(safe_reports_v2))