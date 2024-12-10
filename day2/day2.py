reports = []

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
# Idea: Instead of breaking in report_is_safe if the report fails, we can just calculate the
# number of failed levels, and if it is less than or equal to 1, return true

def report_is_safe_v2(report, problem_dampener = 1):
    # A report is safe if:
    #   1. All levels are either increasing or decreasing
    #   2. Any two adjacent levels differ by at least one and at most 3
    #   3. There can be one unsafe level
    decreasing = None
    report_i = 1
    prev_level = report[0]
    unsafe_levels = 0
    while(report_i < len(report)):
        # First, figure out whether we should be decreasing or increasing
        curr_level = report[report_i]
        if decreasing is None:
            if prev_level == curr_level:
                unsafe_levels += 1
                report_i += 1
                prev_level = curr_level
                break
            decreasing = prev_level - curr_level > 0
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
            unsafe_levels += 1

    return unsafe_levels <= problem_dampener

safe_reports_with_dampener = 0
for report in reports:
    safe_reports_with_dampener += int(report_is_safe_v2(report))

print(safe_reports_with_dampener)